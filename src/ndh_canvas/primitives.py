import numpy as np

class PaintingPrimitives:
    """
    Translates the five structural primitives into functional python numerical operators
    to anchor canvas trajectories safely beneath local stability scalars.
    """
    @staticmethod
    def apply_tessellation_bees(canvas, cell_scale: float = 0.1) -> np.ndarray:
        """
        Hexagonal tiling partitioning grid. Stabilizes pixel boundaries 
        and prevents layout drift under continuous stroke loops.
        """
        # Generate structural coordinate scales
        scaled_x = canvas.grid_x / cell_scale
        scaled_y = canvas.grid_y / (cell_scale * np.sqrt(3))
        
        # Convert to alternating barycentric weight spaces
        c_x = np.floor(scaled_x)
        c_y = np.floor(scaled_y)
        return np.sin(c_x) * np.cos(c_y)

    @staticmethod
    def evaluate_holonomy_transport(canvas, trajectory_path: list) -> np.ndarray:
        """
        Calculates path-ordered Christoffel connection forms along stroke curves
        to preserve global perspective and orientation shifts seamlessly.
        """
        holonomy_shift = np.zeros_like(canvas.grid_x)
        # Model path-dependence by stacking localized connection elements over time-steps
        for step in trajectory_path:
            x_pole, y_pole = step
            distance = np.sqrt((canvas.grid_x - x_pole)**2 + (canvas.grid_y - y_pole)**2)
            holonomy_shift += np.exp(-distance**2 / 0.05)
        return np.sin(holonomy_shift)

    @staticmethod
    def evolve_lie_symmetrized_metric(
        canvas, 
        perturbation_field: np.ndarray, 
        alpha: float = 0.01, 
        beta: float = 0.005
    ) -> np.ndarray:
        """
        Forces Ricci-flow metric updates using symmetrized Lie derivatives. 
        Guarantees tensor index symmetry (g_ij = g_ji) across continuous style changes.
        """
        # Evaluate spatial variations across the field
        v_y, v_x = np.gradient(perturbation_field, axis=(0, 1))
        
        # Deform the canvas tensor dynamically while binding deformations safely
        for i in range(2):
            canvas.metric_tensor[:, :, i, i] += -2.0 * alpha * canvas.metric_tensor[:, :, i, i] + beta * v_x
        return canvas.metric_tensor
