import numpy as np
import pytest
from ndh_canvas.conservation import SymplecticConservationLoop

def test_symplectic_volume_preservation():
    """
    Enforces trace volume neutrality. The geometric mean of the matrix spectrum 
    must remain invariant to guarantee path-reversible state archiving.
    """
    dimensions = 80
    loop = SymplecticConservationLoop(dimensions=dimensions)
    
    # 1. Generate an un-normalized, random perturbation matrix simulating drift distortion
    np.random.seed(42) # Anchor tracking parameters for deterministic verification
    distorted_state = np.random.rand(dimensions, dimensions) * 5.0
    
    # 2. Execute the drift-neutralization loop
    normalized_state = loop.enforce_volume_invariant(distorted_state)
    
    # 3. Extract the singular values of the stabilized state matrix
    _, singular_values, _ = np.linalg.svd(normalized_state)
    geometric_mean = np.exp(np.mean(np.log(singular_values)))
    
    # 4. Assert that the geometric mean of the transformed spectrum is normalized to 1.0
    assert np.isclose(geometric_mean, 1.0, atol=1e-12), "Symplectic trace volume variant breached."
    assert normalized_state.shape == (dimensions, dimensions), "Matrix dimension mutation detected."
