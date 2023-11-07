from graph.related_graph import RelatedGraph
import matplotlib.pyplot as plt

from graph.node import Node
color = ["g", "y", "k", "r"]
from graph.graph import Graph

graph = Graph()
node1 = graph.add_node(1, 3)
node2 = graph.add_node(2, 1)
node3 = graph.add_node(1, 4)
node4 = graph.add_node(5, 1)
node5 = graph.add_node(1, 7)
node6 = graph.add_node(7, 1)

graph.add_edge(node1, node2)
graph.add_edge(node2, node3)
graph.add_edge(node3, node4)
graph.add_edge(node4, node5)
graph.add_edge(node5, node6)

graph.delete_edge(node3, node4)
graph.add_edge(node3, node4)

for i, r in enumerate(graph.get_related_graphs()):
    for node in r.get_nodes():
        plt.plot(node.x, node.y, "b.")
        plt.text(node.x, node.y, node.index, color="r")

for i, r in enumerate(graph.get_related_graphs()):
    for edge in r.get_edges():
        x, y = edge.get_line()
        plt.plot(x, y, color[i])
plt.show()


