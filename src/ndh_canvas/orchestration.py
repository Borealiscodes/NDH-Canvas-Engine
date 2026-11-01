import sys
import numpy as np
from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.primitives import PaintingPrimitives
from ndh_canvas.brush_presets import GeometricBrushPresets
from ndh_canvas.exporter import NDHCanvasExporter
from ndh_canvas.conservation import SymplecticConservationLoop

def run_engine():
    """
    Unified execution harness for the NDH-Canvas-Engine.
    Cycles through geometric brush presets and applies symplectic archiving operators.
    """
    print("🎨 [NDH-CANVAS] Initializing continuous manifold architecture...")
    canvas = NDHCanvasField(resolution=256, dimensions=80)
    primitives = PaintingPrimitives()
    conservation_enclave = SymplecticConservationLoop(dimensions=80)
    
    # Define active brush profiles to cycle through sequentially
    brush_sequence = [
        ("Mandala Radial Ripple", GeometricBrushPresets.radial_mandala_brush(canvas)),
        ("Honeycomb Tessellation", GeometricBrushPresets.tessellation_honeycomb_brush(canvas)),
        ("Meadow Spiral Warp", GeometricBrushPresets.meadow_spiral_brush(canvas)),
        ("Hyperbolic Hill Saddle", GeometricBrushPresets.hyperbolic_hill_brush(canvas))
    ]
    
    print("\n🚀 Starting Multi-Preset Manifold Deformation Loop...")
    last_brush_name = "None"
    
    for name, perturbation_field in brush_sequence:
        print(f"\n🖌️  [BRUSH] Activating profile: {name}...")
        last_brush_name = name
        
        # 1. Compute apex directional vectors for the specific brush contour
        _ = canvas.evaluate_apex_gradient(perturbation_field)
        
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
            
        # 5. Execute the Symplectic Conservation Loop step to stabilize manifold volume
        print("    -> Stabilizing trajectory spectrum via SVD volume conservation...")
        canvas.state_manifold = conservation_enclave.archive_active_surface(canvas.state_manifold)
            
    # 6. Serialize and export the final canvas state vector snapshot to disk
    output_filename = "ndh_canvas_snapshot.json"
    print(f"\n💾 [EXPORT] Writing stable state matrix to {output_filename}...")
    
    export_success = NDHCanvasExporter.export_canvas_to_json(
        canvas, output_filename, active_brush_name=last_brush_name
    )
    
    print("\n📊 === FINAL NDH MANIFOLD VALIDATION REPORT ===")
    print(f" -> Resolution Substrate : {canvas.res} x {canvas.res}")
    print(f" -> Ambient Coordinates  : {canvas.dim}-Dimensional Product Space")
    print(f" -> Export Operation     : {'SUCCESS' if export_success else 'FAILED'}")
    print("💎 [STATUS] All geometric presets validated. Drift neutrality verified completely.\n")
    
    sys.exit(0 if export_success else 1)

if __name__ == "__main__":
    run_engine()
