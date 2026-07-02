"""Atlas graph validator.

Validator modules inspect an AtlasGraph to ensure structural correctness before it is used.
"""

from __future__ import annotations

from .graph import AtlasGraph
from .relationship import RelationshipType


class Validator:
    """Validates an AtlasGraph for structural consistency."""

    def validate(self, graph: AtlasGraph) -> None:
        self._validate_node_ids(graph)
        self._validate_edges(graph)

    def _validate_node_ids(self, graph: AtlasGraph) -> None:
        for node in graph:
            if not node.id or not node.label:
                raise ValueError("All AtlasNode instances must have non-empty id and label.")

    def _validate_edges(self, graph: AtlasGraph) -> None:
        for source, edges in graph.edges.items():
            for edge in edges:
                if edge.source == edge.target:
                    raise ValueError("AtlasEdge source and target must be distinct.")
                if edge.relationship not in RelationshipType:
                    raise ValueError(f"Unsupported relationship type: {edge.relationship}")
