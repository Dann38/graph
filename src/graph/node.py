from typing import Set

class Node:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.neighbors = []

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def add_neighbor(self, node: "Node"):
        self.neighbors.append(node)

    def get_neighbors(self) -> Set["Node"]:
        return set(self.neighbors)
