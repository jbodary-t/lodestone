"""Atlas relationship types.

RelationshipType defines the canonical edge semantics that Atlas supports. These types
describe the dependency, reward, and proximity semantics between Activities.
"""

from enum import StrEnum


class RelationshipType(StrEnum):
    REQUIRES = "requires"
    UNLOCKS = "unlocks"
    REWARDS = "rewards"
    CONSUMES = "consumes"
    PRODUCES = "produces"
    NEARBY = "nearby"
    ALTERNATIVE = "alternative"
    TRANSPORTATION = "transportation"
    FUTURE_DEPENDENCY = "future_dependency"
