/-
Dump the declaration-level dependency graph of a Lean project as JSON Lines.

Run from the target project's root, after `lake build`:

  lake env lean --run /path/to/cairn/lean/extract_deps.lean <RootModule> <ModulePrefix>... > decls.jsonl

It emits one line per constant defined in a module whose name starts with one of the
`ModulePrefix`es: its kind, its module and source position, and the constants used in
its type and in its value (for theorems, the proof term). Constants from any module are
listed as dependencies. Filtering, folding of compiler auxiliaries into their parents and
IDF weighting all happen in Python (`cairn.formal`), so this file stays small and easy to
port across Lean versions.
-/
import Lean

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

def main (args : List String) : IO UInt32 := do
  let root :: prefixes := args
    | IO.eprintln "usage: extract_deps <RootModule> <ModulePrefix>..."; return 1
  let prefixes := if prefixes.isEmpty then [root] else prefixes
  initSearchPath (← findSysroot)
  unsafe enableInitializersExecution
  let env ← importModules #[{ module := root.toName }] {}
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
    let valueDeps := match info.value? (allowOpaque := true) with
      | some v => v.getUsedConstants
      | none => #[]
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
      ("type_deps", namesJson info.type.getUsedConstants),
      ("value_deps", namesJson valueDeps)
    ]
    stdout.putStrLn line.compress
    count := count + 1
  IO.eprintln s!"extract_deps: {count} constants from modules under {prefixes}"
  return 0
