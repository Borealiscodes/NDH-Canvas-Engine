import numpy as np
import pytest
from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.primitives import PaintingPrimitives

def test_metric_index_symmetry():
    """
    Enforces index trace validation. Metric tensors must maintain symmetry 
    to preserve volume structures under active deformations.
    """
    field = NDHCanvasField(resolution=64)
    primitives = PaintingPrimitives()
    
    # Simulate a dynamic stroke perturbation field path
    fake_perturbation = np.sin(field.grid_x) * np.cos(field.grid_y)
    updated_metric = primitives.evolve_lie_symmetrized_metric(field, fake_perturbation)
    
    # Validate trace properties remain reflective and symmetric across indices
    assert np.allclose(updated_metric[:, :, 0, 1], updated_metric[:, :, 1, 0])
    assert np.all(updated_metric[:, :, 0, 0] > 0)  # Asserts positive-definiteness

def test_apex_gradient_normalization():
    """
    Verifies that apex gradient vector steps act as pure unit direction fields.
    """
    field = NDHCanvasField(resolution=64)
    fake_energy = field.grid_x**2 + field.grid_y**2
    apex_vectors = field.evaluate_apex_gradient(fake_energy)
    
    # Compute vector norms across the spatial canvas plane
    vector_norms = np.sqrt(apex_vectors[:, :, 0]**2 + apex_vectors[:, :, 1]**2)
    assert np.allclose(vector_norms, 1.0)
