import os
import json
import numpy as np
import pytest
from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.exporter import NDHCanvasExporter

def test_json_export_structure(tmp_path):
    """
    Enforces structural data integrity. The exported file container must 
    exist, parse as legal JSON, and maintain explicit layout tags.
    """
    field = NDHCanvasField(resolution=64)
    target_file = os.path.join(tmp_path, "canvas_snapshot.json")
    
    # 1. Execute the serialization sweep
    export_success = NDHCanvasExporter.export_canvas_to_json(
        field, target_file, active_brush_name="Test_Verification_Profile"
    )
    
    # 2. Assert file execution operations passed cleanly
    assert export_success is True
    assert os.path.exists(target_file)
    
    # 3. Read back the file payload and verify type structures
    with open(target_file, "r", encoding="utf-8") as f:
        parsed_data = json.load(f)
        
    assert parsed_data["metadata"]["active_brush"] == "Test_Verification_Profile"
    assert parsed_data["metadata"]["resolution"] == 64
    assert parsed_data["tensor_invariants"]["is_symmetric"] is True
    assert isinstance(parsed_data["compressed_manifold_coordinates"], list)
