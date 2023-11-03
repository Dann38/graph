from src.graph.related_graph import RelatedGraph
import matplotlib.pyplot as plt

from src.graph.node import Node


node1 = Node(1, 3)
node2 = Node(2, 1)
node3 = Node(1, 4)
node4 = Node(5, 1)
node5 = Node(1, 7)
node6 = Node(7, 1)


r1 = RelatedGraph(node1)
r1.add_node(node2, node1)
r1.add_node(node3, node2)
r1.add_node(node4, node3)
r1.add_node(node5, node4)
r1.add_node(node6, node5)
r1.add_edge(node3, node1)

r1.delete_edge_from_nodes(node3, node4)

for node in r1.get_nodes():
    plt.plot(node.x, node.y, "bo")

for edge in r1.get_edges():
    x, y = edge.get_line()
    plt.plot(x, y, "g")
plt.show()
