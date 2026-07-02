"""Atlas edge representation.

AtlasEdge defines directed connections between AtlasNode instances. Each edge carries a
RelationshipType describing how the nodes are connected.
"""

from __future__ import annotations

from dataclasses import dataclass
from .relationship import RelationshipType


@dataclass
class AtlasEdge:
    """A directed relationship between two nodes."""

    source: str
    target: str
    relationship: RelationshipType
    metadata: dict[str, str] = None

    def __post_init__(self) -> None:
        if not self.source or not self.target:
            raise ValueError("AtlasEdge source and target must be non-empty.")
        if self.metadata is None:
            self.metadata = {}
