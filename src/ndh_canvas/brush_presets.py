import numpy as np

class GeometricBrushPresets:
    """
    Defines structural brush preset fields that modulate the canvas manifold
    under different geometric configurations.
    """
    
    @staticmethod
    def radial_mandala_brush(canvas, frequency: float = 4.0) -> np.ndarray:
        """
        MANDALA COGNITION PRESET: Creates symmetric radial ripples around the origin.
        """
        radius = np.sqrt(canvas.grid_x**2 + canvas.grid_y**2)
        # Avoid poles at the origin
        safe_radius = np.where(radius == 0, 1e-12, radius)
        return np.cos(frequency * np.pi * safe_radius)

    @staticmethod
    def tessellation_honeycomb_brush(canvas, scale: float = 0.2) -> np.ndarray:
        """
        TESSELLATION BEES PRESET: Generates structured, interlocking hexagonal boundary blocks.
        """
        val_x = np.sin(canvas.grid_x / scale)
        val_y = np.cos(canvas.grid_y / (scale * np.sqrt(3)))
        return val_x * val_y

    @staticmethod
    def meadow_spiral_brush(canvas, tightness: float = 2.0) -> np.ndarray:
        """
        MEADOW PEDAGOGY PRESET: Computes a path-dependent spiral coordinate warp.
        """
        angle = np.arctan2(canvas.grid_y, canvas.grid_x)
        radius = np.sqrt(canvas.grid_x**2 + canvas.grid_y**2)
        return np.sin(tightness * radius + angle)

    @staticmethod
    def hyperbolic_hill_brush(canvas) -> np.ndarray:
        """
        MANIFOLD GOATS PRESET: Generates explicit saddle curvatures over the coordinate grid.
        """
        return canvas.grid_x**2 - canvas.grid_y**2
