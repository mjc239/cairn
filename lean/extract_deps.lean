/-
Dump the declaration-level dependency graph of a Lean project as JSON Lines.

Run from the target project's root, after `lake build`:

  lake env lean --run /path/to/cairn/lean/extract_deps.lean <RootModule> <ModulePrefix>... > decls.jsonl

It emits one line per constant defined in a module whose name starts with one of the
`ModulePrefix`es: its kind, its module and source position, and the constants used in
its type and in its value (for theorems, the proof term),
plus the size of both terms (number of distinct `Expr` objects). For user-facing constants it also
records the docstring, the pretty-printed statement (`type_pp`) and a short form (`stmt_short`)
showing only explicit arguments and hypotheses, as in Mathlib's documentation. Constants from any module are
listed as dependencies. Filtering, folding of compiler auxiliaries into their parents and
IDF weighting all happen in Python (`cairn.formal`), so this file stays small and easy to
port across Lean versions.
-/
import Lean
import Lean.Util.NumObjs

open Lean

def kindOf : ConstantInfo → String
  | .thmInfo _    => "theorem"
  | .defnInfo _   => "def"
  | .axiomInfo _  => "axiom"
  | .opaqueInfo _ => "opaque"
  | .inductInfo _ => "inductive"
  | .ctorInfo _   => "constructor"
  | .recInfo _    => "recursor"
  | .quotInfo _   => "quot"

def namesJson (ns : Array Name) : Json :=
  Json.arr (ns.map (fun n => Json.str n.toString))

/-- Pretty-print a statement; failures (rare) become an empty string rather than aborting the dump. -/
def ppType (env : Environment) (e : Expr) : IO String := do
  let opts : Options := (({} : Options).set `format.width (100 : Nat)).setBool `pp.proofs false
  let ctx : Core.Context := { fileName := "<cairn>", fileMap := default, options := opts, maxHeartbeats := 0 }
  try
    let (fmt, _, _) ← (Meta.ppExpr e).toIO ctx { env }
    return toString fmt
  catch _ =>
    return ""

/-- Short statement: explicit binders, meaningful instance assumptions and the conclusion, e.g.
`[Finite G] (hA : A.Nonempty) : …`. Implicit binders are dropped, and so are instance binders that only
equip a variable with structure (`[AddCommGroup G]`, `[MeasurableSpace Ω]`: a class applied to bound
variables only, not a proposition). Instances that are propositions (`[Finite G]`, `[IsProbabilityMeasure μ]`)
or mention other terms (`[Module (ZMod 2) G]`) are kept. Unnamed hypotheses print as `(_ : P)`. -/
def ppShort (env : Environment) (e : Expr) : IO String := do
  let opts : Options := (({} : Options).set `format.width (100 : Nat)).setBool `pp.proofs false
  let ctx : Core.Context := { fileName := "<cairn>", fileMap := default, options := opts, maxHeartbeats := 0 }
  let go : MetaM String := Meta.forallTelescope e fun xs body => do
    let mut parts : Array String := #[]
    for x in xs do
      let d ← x.fvarId!.getDecl
      if d.binderInfo.isExplicit then
        let name := if d.userName.hasMacroScopes then "_" else d.userName.toString
        parts := parts.push s!"({name} : {← Meta.ppExpr d.type})"
      else if d.binderInfo.isInstImplicit then
        let structural := !(← Meta.isProp d.type) && d.type.getAppArgs.all (·.isFVar)
        unless structural do
          parts := parts.push s!"[{← Meta.ppExpr d.type}]"
    let concl := toString (← Meta.ppExpr body)
    return if parts.isEmpty then concl else " ".intercalate parts.toList ++ " : " ++ concl
  try
    let (str, _, _) ← go.toIO ctx { env }
    return str
  catch _ =>
    return ""

def main (args : List String) : IO UInt32 := do
  let root :: prefixes := args
    | IO.eprintln "usage: extract_deps <RootModule> <ModulePrefix>..."; return 1
  let prefixes := if prefixes.isEmpty then [root] else prefixes
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  let env ← importModules #[{ module := root.toName }] {} (loadExts := true)
  let modNames := env.allImportedModuleNames
  let inProject (m : Name) : Bool := prefixes.any fun p => p.toName.isPrefixOf m
  let stdout ← IO.getStdout
  let mut count := 0
  for (name, info) in env.constants.map₁.toList do
    let some idx := env.getModuleIdxFor? name | continue
    let some mod := modNames[idx.toNat]? | continue
    unless inProject mod do continue
    let range := declRangeExt.find? (level := .exported) env name <|>
      declRangeExt.find? (level := .server) env name
    let value := info.value? (allowOpaque := true)
    let valueDeps := match value with
      | some v => v.getUsedConstants
      | none => #[]
    let valueSize ← match value with
      | some v => v.numObjs
      | none => pure 0
    let typeSize ← info.type.numObjs
    let userFacing := !(privateToUserName name).isInternalDetail
    let doc ← if userFacing then findSimpleDocString? env name else pure none
    let typePP ← if userFacing then ppType env info.type else pure ""
    let stmtShort ← if userFacing then ppShort env info.type else pure ""
    let line := Json.mkObj [
      ("name", Json.str name.toString),
      ("user_name", Json.str (privateToUserName name).toString),
      ("private", Json.bool (isPrivateName name)),
      ("module", Json.str mod.toString),
      ("kind", Json.str (kindOf info)),
      ("internal", Json.bool (privateToUserName name).isInternalDetail),
      ("matcher", Json.bool (Meta.isMatcherCore env name)),
      ("aux_recursor", Json.bool (isAuxRecursor env name || isNoConfusion env name)),
      ("line", match range with
        | some r => Json.num r.range.pos.line
        | none => Json.null),
      ("type_size", Json.num typeSize),
      ("doc", match doc with
        | some d => Json.str d
        | none => Json.null),
      ("type_pp", Json.str typePP),
      ("stmt_short", Json.str stmtShort),
      ("value_size", Json.num valueSize),
      ("type_deps", namesJson info.type.getUsedConstants),
      ("value_deps", namesJson valueDeps)
    ]
    stdout.putStrLn line.compress
    count := count + 1
  IO.eprintln s!"extract_deps: {count} constants from modules under {prefixes}"
  return 0
