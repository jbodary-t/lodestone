"""Provider interface for Atlas.

Providers are responsible for supplying Atlas with nodes and edges. Providers must
implement the contract without encoding any game-specific rules.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable
from .node import AtlasNode
from .edge import AtlasEdge


class Provider(ABC):
    """Interface for Atlas data providers."""

    @abstractmethod
    def nodes(self) -> Iterable[AtlasNode]:
        """Return all nodes supplied by the provider."""
        raise NotImplementedError

    @abstractmethod
    def edges(self) -> Iterable[AtlasEdge]:
        """Return all edges supplied by the provider."""
        raise NotImplementedError

    @abstractmethod
    def name(self) -> str:
        """Return the provider's stable name."""
        raise NotImplementedError
