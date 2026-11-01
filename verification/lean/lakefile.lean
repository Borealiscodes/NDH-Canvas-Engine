import Lake
open Lake DSL

package «ndh_canvas_verification» where
  -- Add package configuration options here
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩ -- Enforces clean unicode printing for operators
  ]

@[default_target]
lean_lib «NdhCanvasVerification» where
  srcDir := "src"

require mathlib from git
  "https://github.com" @ "v4.15.0"
