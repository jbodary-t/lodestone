"""Atlas importer.

The importer coordinates provider data ingestion and graph construction. It does not
interpret game data itself; it simply transforms provider-supplied nodes and edges into Atlas.
"""

from __future__ import annotations

from typing import Iterable
from .graph import AtlasGraph
from .node import AtlasNode
from .edge import AtlasEdge
from .provider import Provider
from .validator import Validator


class Importer:
    """Constructs an AtlasGraph from one or more providers."""

    def __init__(self, validator: Validator | None = None) -> None:
        self.validator = validator

    def import_providers(self, providers: Iterable[Provider]) -> AtlasGraph[AtlasNode]:
        graph = AtlasGraph[AtlasNode]()
        for provider in providers:
            for node in provider.nodes():
                graph.add_node(node)
            for edge in provider.edges():
                graph.add_edge(edge)
        if self.validator is not None:
            self.validator.validate(graph)
        return graph
