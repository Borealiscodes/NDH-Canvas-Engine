import sys
import numpy as np
from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.primitives import PaintingPrimitives

def run_engine():
    """
    Unified execution harness for the NDH-Canvas-Engine.
    Simulates a continuous stroke sequence over a curved Riemannian manifold.
    """
    print("🎨 [NDH-CANVAS] Initializing continuous manifold architecture...")
    
    # 1. Instantiate the canvas manifold (Resolution 256 for rapid local evaluation)
    canvas = NDHCanvasField(resolution=256, dimensions=80)
    primitives = PaintingPrimitives()
    
    # 2. Simulate a non-linear stroke energy curve (Mandalic radial distribution)
    print("🌀 [NDH-CANVAS] Constructing radial energy potential field...")
    radius_squared = canvas.grid_x**2 + canvas.grid_y**2
    stroke_potential = np.sin(5.0 * np.pi * np.sqrt(radius_squared)) * np.exp(-radius_squared)
    
    # 3. Evaluate unit directional trajectories via Apex Gradients
    print("📐 [NDH-CANVAS] Computing apex gradient steering vectors...")
    apex_gradient_field = canvas.evaluate_apex_gradient(stroke_potential)
    
    # 4. Check the manifold area for forced administrative collapse anomalies
    print("💥 [NDH-CANVAS] Screening mesh terrain for collapse surface boundaries...")
    collapse_mask = canvas.check_collapse_surface(stroke_potential)
    collapse_count = np.sum(collapse_mask)
    
    # 5. Model stroke path-dependence by feeding steps to the Holonomy loop
    print("🌾 [NDH-CANVAS] Commencing path-ordered holonomy transport loop...")
    simulated_trajectory = [(-0.5, -0.5), (0.0, 0.2), (0.5, -0.5)]
    holonomy_matrix = primitives.evaluate_holonomy_transport(canvas, simulated_trajectory)
    
    # 6. Force metric evolution under index-symmetric Lie derivatives
    print("🐝 [NDH-CANVAS] Evaporating curvature drift via Lie-symmetrized metric updates...")
    tessellation_grid = primitives.apply_tessellation_bees(canvas, cell_scale=0.15)
    updated_metric = primitives.evolve_lie_symmetrized_metric(canvas, tessellation_grid)
    
    # Assert structural integrity and trace validation before completing execution
    symmetry_error = np.max(np.abs(updated_metric[:, :, 0, 1] - updated_metric[:, :, 1, 0]))
    
    print("\n📊 === NDH MANIFOLD VALIDATION REPORT ===")
    print(f" -> Resolution Substrate : {canvas.res} x {canvas.res}")
    print(f" -> Ambient Coordinates  : {canvas.dim}-Dimensional Product Space")
    print(f" -> Collapse Intercepts  : {collapse_count} coordinates masked")
    print(f" -> Tensor Symmetry Delta: {symmetry_error:.12f}")
    
    if symmetry_error < 1e-12:
        print("💎 [STATUS] Invariant drift neutrality verified. Canvas processing complete.\n")
        sys.exit(0)
    else:
        print("🚨 [CRITICAL] Structural asymmetry detected within the manifold matrix.\n")
        sys.exit(1)

if __name__ == "__main__":
    run_engine()
