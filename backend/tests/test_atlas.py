import pytest
import uuid

from app.atlas.cache import Cache
from app.atlas.edge import AtlasEdge
from app.atlas.graph import AtlasGraph
from app.atlas.importer import Importer
from app.atlas.node import AtlasNode
from app.atlas.relationship import RelationshipType
from app.atlas.validator import Validator
from app.atlas.provider import Provider


class DummyProvider(Provider):
    def __init__(self, nodes, edges):
        self._nodes = nodes
        self._edges = edges

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges

    def name(self):
        return "dummy"


def test_atlas_node_requires_non_empty_id_and_label():
    with pytest.raises(ValueError):
        AtlasNode(id="", label="label")
    with pytest.raises(ValueError):
        AtlasNode(id=str(uuid.uuid4()), label="")


def test_graph_add_and_retrieve_node():
    graph = AtlasGraph[AtlasNode]()
    node = AtlasNode(id="node-1", label="Activity One")
    graph.add_node(node)

    assert graph.has_node("node-1")
    assert graph.get_node("node-1") == node


def test_graph_add_edge_requires_existing_nodes():
    graph = AtlasGraph[AtlasNode]()
    node1 = AtlasNode(id="node-1", label="Activity One")
    node2 = AtlasNode(id="node-2", label="Activity Two")
    graph.add_node(node1)

    edge = AtlasEdge(source="node-1", target="node-2", relationship=RelationshipType.REQUIRES)
    with pytest.raises(ValueError):
        graph.add_edge(edge)


def test_graph_add_edge_and_neighbors():
    graph = AtlasGraph[AtlasNode]()
    node1 = AtlasNode(id="node-1", label="Activity One")
    node2 = AtlasNode(id="node-2", label="Activity Two")
    graph.add_node(node1)
    graph.add_node(node2)

    edge = AtlasEdge(source="node-1", target="node-2", relationship=RelationshipType.REQUIRES)
    graph.add_edge(edge)

    assert graph.outgoing_edges("node-1") == [edge]
    assert list(graph.neighbors("node-1")) == [node2]
    assert graph.incoming_edges("node-2") == [edge]


def test_importer_loads_provider_data_and_validates():
    graph = AtlasGraph[AtlasNode]()
    node1 = AtlasNode(id="node-1", label="Activity One")
    node2 = AtlasNode(id="node-2", label="Activity Two")
    edge = AtlasEdge(source="node-1", target="node-2", relationship=RelationshipType.UNLOCKS)

    provider = DummyProvider(nodes=[node1, node2], edges=[edge])
    importer = Importer(validator=Validator())
    loaded_graph = importer.import_providers([provider])

    assert loaded_graph.has_node("node-1")
    assert loaded_graph.has_node("node-2")
    assert loaded_graph.outgoing_edges("node-1")[0].relationship == RelationshipType.UNLOCKS


def test_validator_rejects_self_referential_edge():
    graph = AtlasGraph[AtlasNode]()
    node = AtlasNode(id="node-1", label="Activity One")
    graph.add_node(node)
    graph.add_edge(AtlasEdge(source="node-1", target="node-1", relationship=RelationshipType.REQUIRES))

    validator = Validator()
    with pytest.raises(ValueError):
        validator.validate(graph)


def test_cache_stores_and_retrieves_graph():
    cache = Cache()
    graph = AtlasGraph[AtlasNode]()
    node = AtlasNode(id="node-1", label="Activity One")
    graph.add_node(node)

    cache.store(graph)
    assert cache.retrieve() == graph
    cache.clear()
    assert cache.retrieve() is None
