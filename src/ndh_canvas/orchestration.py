import sys
import numpy as np
from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.primitives import PaintingPrimitives
from ndh_canvas.brush_presets import GeometricBrushPresets

def run_engine():
    """
    Unified execution harness for the NDH-Canvas-Engine.
    Simulates cross-modular stroke sequences across alternating geometric brush presets.
    """
    print("🎨 [NDH-CANVAS] Initializing continuous manifold architecture...")
    canvas = NDHCanvasField(resolution=256, dimensions=80)
    primitives = PaintingPrimitives()
    
    # Define active brush profiles to cycle through sequentially
    brush_sequence = [
        ("Mandala Radial Ripple", GeometricBrushPresets.radial_mandala_brush(canvas)),
        ("Honeycomb Tessellation", GeometricBrushPresets.tessellation_honeycomb_brush(canvas)),
        ("Meadow Spiral Warp", GeometricBrushPresets.meadow_spiral_brush(canvas)),
        ("Hyperbolic Hill Saddle", GeometricBrushPresets.hyperbolic_hill_brush(canvas))
    ]
    
    print("\n🚀 Starting Multi-Preset Manifold Deformation Loop...")
    
    for name, perturbation_field in brush_sequence:
        print(f"\n🖌️  [BRUSH] Activating profile: {name}...")
        
        # 1. Compute apex directional vectors for the specific brush contour
        apex_gradient_field = canvas.evaluate_apex_gradient(perturbation_field)
        
        # 2. Check for local Hessian discontinuities before applying deformation
        collapse_mask = canvas.check_collapse_surface(perturbation_field)
        collapse_count = np.sum(collapse_mask)
        
        # 3. Evolve the Riemannian metric tensor under Lie-symmetrized derivatives
        updated_metric = primitives.evolve_lie_symmetrized_metric(canvas, perturbation_field)
        
        # 4. Measure index symmetry error delta to guarantee drift neutrality
        symmetry_error = np.max(np.abs(updated_metric[:, :, 0, 1] - updated_metric[:, :, 1, 0]))
        
        print(f"    -> Collapse Intercepts  : {collapse_count} coordinates masked")
        print(f"    -> Tensor Symmetry Delta: {symmetry_error:.12f}")
        
        if symmetry_error > 1e-12:
            print(f"🚨 [CRITICAL] Structural asymmetry detected in brush profile: {name}")
            sys.exit(1)
            
    print("\n📊 === FINAL NDH MANIFOLD VALIDATION REPORT ===")
    print(f" -> Resolution Substrate : {canvas.res} x {canvas.res}")
    print(f" -> Ambient Coordinates  : {canvas.dim}-Dimensional Product Space")
    print("💎 [STATUS] All geometric presets validated. Drift neutrality verified completely.\n")
    sys.exit(0)

if __name__ == "__main__":
    run_engine()
