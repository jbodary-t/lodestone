"""Atlas node representation.

AtlasNode represents a generic graph node. It stores an identifier and optional metadata
that can be used by higher-level systems without the graph needing to understand the data.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AtlasNode:
    """A generic graph node in Atlas."""

    id: str
    label: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("AtlasNode id must not be empty.")
        if not self.label:
            raise ValueError("AtlasNode label must not be empty.")
