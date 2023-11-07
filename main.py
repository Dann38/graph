from src.graph.related_graph import RelatedGraph
import matplotlib.pyplot as plt

from src.graph.node import Node
color = ["g", "y", "k", "r"]
from src.graph.graph import Graph

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

# node1 = Node(1, 3, index=1)
# node2 = Node(2, 1, index=2)
# node3 = Node(1, 4, index=3)
# node4 = Node(5, 1, index=4)
# node5 = Node(1, 7, index=5)
# node6 = Node(7, 1, index=6)
#
#
# r1 = RelatedGraph(node1)
# r1.add_node(node2, node1)
# r1.add_node(node3, node2)
# r1.add_node(node4, node3)
# r1.add_node(node5, node4)
# r1.add_node(node6, node5)
# # r1.add_edge(node3, node5)
#
# list_r = r1.delete_edge_from_nodes(node3, node4)
#
# list_r[0].add_related_graph(list_r[1], node3, node5)
#
#
# node7 = Node(8, 8, index=7)
# node8 = Node(6, 6, index=8)
# node9 = Node(8, 6, index=9)
# r2 = RelatedGraph(node7)
# r2.add_node(node8, node7)
# r2.add_node(node9, node7)
# r2.add_edge(node8, node9)
#
#
# list_r[0].add_related_graph(r2, this_node=node6, other_node=node9)
# list_r = [list_r[0]]
# # list_r = [list_r[0], r2]
#
# for i, r in enumerate(list_r):
#     for node in r.get_nodes():
#         plt.plot(node.x, node.y, "b.")
#         plt.text(node.x, node.y, node.index, color="r")
#
# for i, r in enumerate(list_r):
#     for edge in r.get_edges():
#         x, y = edge.get_line()
#         plt.plot(x, y, color[i])
# plt.show()

