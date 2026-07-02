"""Atlas graph foundation.

This module defines a generic directed dependency graph. Atlas uses this graph to represent
activities as nodes and their relationships as edges. The graph is intentionally generic
and does not encode any RuneScape-specific vocabulary.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


@dataclass
class AtlasGraph(Generic[T]):
    """A directed graph of nodes and edges.

    Nodes are unique by their identifier. Edges represent typed relationships between nodes.
    """

    nodes: dict[str, T] = field(default_factory=dict)
    edges: dict[str, list[AtlasEdge[T]]] = field(default_factory=dict)

    def add_node(self, node: T) -> None:
        """Add a node to the graph. If the node already exists, the operation is idempotent."""
        self.nodes[node.id] = node
        self.edges.setdefault(node.id, [])

    def add_edge(self, edge: "AtlasEdge[T]") -> None:
        """Add a directed edge to the graph."""
        if edge.source not in self.nodes or edge.target not in self.nodes:
            raise ValueError("Both source and target must exist in the graph before adding an edge.")
        self.edges.setdefault(edge.source, []).append(edge)

    def get_node(self, node_id: str) -> T | None:
        """Return a node by its identifier."""
        return self.nodes.get(node_id)

    def neighbors(self, node_id: str, relationship: RelationshipType | None = None) -> Iterator[T]:
        """Iterate over neighbors of a node optionally filtered by relationship type."""
        for edge in self.edges.get(node_id, []):
            if relationship is None or edge.relationship == relationship:
                yield self.nodes[edge.target]

    def outgoing_edges(self, node_id: str) -> list["AtlasEdge[T]"]:
        """Return the list of edges originating from a node."""
        return list(self.edges.get(node_id, []))

    def incoming_edges(self, node_id: str) -> list["AtlasEdge[T]"]:
        """Return the list of edges terminating at a node."""
        return [edge for edges in self.edges.values() for edge in edges if edge.target == node_id]

    def has_node(self, node_id: str) -> bool:
        """Check whether a node exists in the graph."""
        return node_id in self.nodes

    def __iter__(self) -> Iterator[T]:
        return iter(self.nodes.values())
