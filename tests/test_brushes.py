import numpy as np
import pytest
from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.brush_presets import GeometricBrushPresets

def test_brush_numerical_stability():
    """
    Enforces boundary stability. Every geometric preset brush must evaluate
    to finite real numbers across the entire canvas grid.
    """
    field = NDHCanvasField(resolution=64)
    
    presets = [
        GeometricBrushPresets.radial_mandala_brush(field),
        GeometricBrushPresets.tessellation_honeycomb_brush(field),
        GeometricBrushPresets.meadow_spiral_brush(field),
        GeometricBrushPresets.hyperbolic_hill_brush(field)
    ]
    
    for brush_output in presets:
        assert np.all(np.isfinite(brush_output)), "Brush generated non-finite boundary values."
        assert brush_output.shape == (64, 64), "Brush output dimensions do not match coordinate grid."

def test_mandala_axial_symmetry():
    """
    Verifies that the radial mandala brush preserves perfect, 
    un-governed reflective symmetry across mirror coordinate planes.
    """
    field = NDHCanvasField(resolution=64)
    brush_output = GeometricBrushPresets.radial_mandala_brush(field)
    
    # Flip the matrix horizontally and vertically to test radial coherence
    flipped_lr = np.fliplr(brush_output)
    flipped_ud = np.flipud(brush_output)
    
    assert np.allclose(brush_output, flipped_lr, atol=1e-12), "Mandala lost horizontal symmetry."
    assert np.allclose(brush_output, flipped_ud, atol=1e-12), "Mandala lost vertical symmetry."
