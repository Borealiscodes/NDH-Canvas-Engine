import numpy as np

class NDHCanvasField:
    """
    Implements a curved Riemannian visual manifold using explicit 
    differential operators for non-linear paint deformations.
    """
    def __init__(self, resolution: int = 512, dimensions: int = 80):
        self.res = resolution
        self.dim = dimensions
        # Initialize flat coordinates then map to standard curved manifold parameters
        self.grid_x, self.grid_y = np.meshgrid(
            np.linspace(-1, 1, resolution),
            np.linspace(-1, 1, resolution)
        )
        # Structural state vector array z(t) over the coordinate space
        self.state_manifold = np.zeros((resolution, resolution, dimensions))
        # Initial symmetric metric tensor g_ij representing default canvas density
        self.metric_tensor = np.zeros((resolution, resolution, 2, 2))
        for i in range(2):
            self.metric_tensor[:, :, i, i] = 1.0

    def evaluate_apex_gradient(self, energy_functional: np.ndarray) -> np.ndarray:
        """
        Evaluates the unit vector field identifying the steepest ascent direction 
        of stroke energy curves: grad_apex = grad(E) / ||grad(E)||
        """
        grad_y, grad_x = np.gradient(energy_functional)
        magnitude = np.sqrt(grad_x**2 + grad_y**2)
        # Avoid division by zero anomalies dynamically along saddle contours
        magnitude[magnitude == 0] = 1e-12
        return np.stack([grad_x / magnitude, grad_y / magnitude], axis=-1)

    def evaluate_9d_radial_laplacian(self, radius_matrix: np.ndarray) -> np.ndarray:
        """
        Damps localized high-frequency curvature fluctuations during stroke execution
        using the 9D radial Laplacian operator trace layout: Δ_9 f(r) = f''(r) + (8/r) f'(r)
        """
        # Calculate localized spatial derivatives
        f_prime = np.gradient(radius_matrix, axis=0)
        f_double_prime = np.gradient(f_prime, axis=0)
        
        # Guard against zero-radius poles at stroke origins
        safe_r = np.where(radius_matrix == 0, 1e-12, radius_matrix)
        laplacian_trace = f_double_prime + (8.0 / safe_r) * f_prime
        return laplacian_trace

    def check_collapse_surface(self, stroke_potential: np.ndarray) -> np.ndarray:
        """
        Locates the Collapse Surface C(z) boundary mapping where 
        the state potential Hessian loses positive-definiteness: det(grad^2 z) < 0
        """
        grad_y, grad_x = np.gradient(stroke_potential)
        h_yy, h_yx = np.gradient(grad_y)
        h_xy, h_xx = np.gradient(grad_x)
        
        # Calculate explicit local determinant boundaries
        hessian_determinant = (h_xx * h_yy) - (h_xy * h_yx)
        collapse_mask = hessian_determinant < 0
        return collapse_mask
