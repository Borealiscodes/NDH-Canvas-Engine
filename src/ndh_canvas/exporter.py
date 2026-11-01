import json
import numpy as np

class NDHCanvasExporter:
    """
    Serializes and compresses the active geometric canvas state vector 
    and metric configurations into lightweight JSON file containers.
    """
    
    @staticmethod
    def export_canvas_to_json(canvas, file_path: str, active_brush_name: str) -> bool:
        """
        Extracts trace metrics and state parameters, converting numpy arrays
        into standard python lists for structured JSON storage.
        """
        # Compress the massive 80D space down to critical layout anchors for rapid export
        sampled_indices = [0, 10, 20, 40, 60, 79]
        compressed_manifold = canvas.state_manifold[::16, ::16, sampled_indices]
        
        # Structure the canvas layout metadata entries
        state_payload = {
            "metadata": {
                "engine_version": "1.0.0",
                "resolution": canvas.res,
                "ambient_dimensions": canvas.dim,
                "active_brush": active_brush_name
            },
            "tensor_invariants": {
                "mean_metric_density_g00": float(np.mean(canvas.metric_tensor[:, :, 0, 0])),
                "mean_metric_density_g11": float(np.mean(canvas.metric_tensor[:, :, 1, 1])),
                "is_symmetric": bool(np.allclose(canvas.metric_tensor[:, :, 0, 1], canvas.metric_tensor[:, :, 1, 0]))
            },
            "compressed_manifold_coordinates": compressed_manifold.tolist()
        }
        
        try:
            with open(file_path, "w", encoding="utf-8") as target_file:
                json.dump(state_payload, target_file, indent=2)
            return True
        except IOError as error:
            print(f"🚨 [EXPORT ERROR] Failed to write structural state container: {error}")
            return False
