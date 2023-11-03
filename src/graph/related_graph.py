from .node import Node
from .edge import Edge

from typing import List


class RelatedGraph:
    def __init__(self, node: Node):
        self.nodes = {node: 1}
        self.edges = dict()
        self.count_nodes = 1

    def get_nodes(self) -> List[Node]:
        return list(self.nodes.keys())

    def add_node(self, node: Node, node_connect: Node):
        if not (node_connect in self.nodes):
            print("НЕТ УЗЛА ДЛЯ СОЕДИНЕНИЯ")
            return
        if not (node in self.nodes):
            self.count_nodes += 1
            self.nodes[node] = self.count_nodes
        self.add_edge(node, node_connect)

    def add_edge(self, node1: Node, node2: Node):
        if not (node1 in self.nodes) or not (node2 in self.nodes):
            print("НЕТ ТАКИХ УЗЛОВ")
            return
        keys_edge = tuple({self.nodes[node1], self.nodes[node2]})
        if (keys_edge in self.edges):
            print("УЗЕЛ УЖЕ ЕСТЬ")
        self.edges[keys_edge] = Edge({node1, node2})
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def get_edges(self) -> List[Edge]:
        return [edge for key_edge, edge in self.edges.items()]

    def get_edge_from_nodes(self, node1: Node, node2: Node) -> Edge:
        key_edge = tuple({self.nodes[node1], self.nodes[node2]})
        return self.edges[key_edge]

    def delete_edge(self, edge: Edge):
        node1, node2 = edge.get_nodes()
        self.delete_edge_from_nodes(node1, node2)

    def delete_edge_from_nodes(self, node1: Node, node2: Node):
        # TODO Проверка на существование
        key_edge = tuple({self.nodes[node1], self.nodes[node2]})
        self.edges.pop(key_edge)
        neighbors_node1 = node1.get_neighbors()
        neighbors_node2 = node2.get_neighbors()

        graph1_nodes = []
        graph1_edges_key = set()
        sub_set = neighbors_node1.intersection(neighbors_node2.union({node2}))
        if len(sub_set) > 1:
            return [self]

        nodes = neighbors_node1 - sub_set

        while len(nodes) != 0:
            node = nodes.pop()
            if not (node in graph1_nodes):
                graph1_nodes.append(node)
            if node == node2:
                return [self]
            nodes_new = node.get_neighbors()
            for node_new in nodes_new:
                keys_edge_new = tuple({self.nodes[node_new], self.nodes[node]})
                graph1_edges_key.add(keys_edge_new)
            nodes.union(nodes_new)

        graph2_edges_key = set(self.edges.keys()) - graph1_edges_key
        graph1 = self.create_related_graph(graph1_edges_key)
        graph2 = self.create_related_graph(graph2_edges_key)
        return graph1, graph2

        print("graph1")
        for key in graph1_edges_key:
            ns2 = self.edges[key].get_nodes()
            print(ns2[0], "---", ns2[1])

        print("graph2")
        for key in graph2_edges_key:
            ns2 = self.edges[key].get_nodes()
            print(ns2[0], "---", ns2[1])

    def create_related_graph(self, edges_key) -> "RelatedGraph":

        key = edges_key.pop()
        nodes = self.edges[key]
        r = RelatedGraph(nodes[0])
        r.add_node(nodes[1], nodes[0])

        for key in edges_key:
            nodes = self.edges[key].get_nodes()
            print(nodes[0], "---", nodes[1])

        return r