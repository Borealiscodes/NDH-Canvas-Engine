"""
NDH-Canvas-Engine Namespace Substrate
Exposes explicit non-linear geometric operators and painting primitives 
under unified, absolute packaging import pathways.
"""

from ndh_canvas.canvas_core import NDHCanvasField
from ndh_canvas.primitives import PaintingPrimitives
from ndh_canvas.brush_presets import GeometricBrushPresets
from ndh_canvas.exporter import NDHCanvasExporter
from ndh_canvas.conservation import SymplecticConservationLoop

__all__ = [
    "NDHCanvasField",
    "PaintingPrimitives",
    "GeometricBrushPresets",
    "NDHCanvasExporter",
    "SymplecticConservationLoop",
]

__version__ = "1.1.0" # Bump minor version to track structural update
__author__ = "Borealis S. Hedling"
