"""Atlas cache layer.

The cache stores graph snapshots for fast reuse and can be extended with provider-aware caching.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from .graph import AtlasGraph
from .node import AtlasNode


@dataclass
class Cache:
    """A simple cache for Atlas graphs."""

    graph: AtlasGraph[AtlasNode] | None = None

    def store(self, graph: AtlasGraph[AtlasNode]) -> None:
        self.graph = graph

    def retrieve(self) -> AtlasGraph[AtlasNode] | None:
        return self.graph

    def clear(self) -> None:
        self.graph = None
