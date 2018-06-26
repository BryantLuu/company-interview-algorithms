class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = set()

class Graph:
    def __init__(self):
        self.nodes = dict()

    def addLink(self, a, b):
        if a in self.nodes:
            self.nodes[a].neighbors.add(b)
        else:
            self.nodes[a] = Node(a)
            self.nodes[a].neighbors.add(b)
        if b in self.nodes:
            self.nodes[b].neighbors.add(a)
        else:
            self.nodes[b] = Node(b)
            self.nodes[b].neighbors.add(a)

    def removeLink(self, a, b):
        if self.nodes[a] and b in self.nodes[a].neighbors:
            self.nodes[a].neighbors.remove(b)
        if self.nodes[b] and a in self.nodes[b].neighbors:
            self.nodes[b].neighbors.remove(a)

    def isLinked(self, a, b):
        if a not in self.nodes:
            return False
        if b not in self.nodes:
            return False
        visited = set()
        node = self.nodes[a]
        visited.add(node.id)
        def checkIsLinked(nodes_ids, id):
            for node_id in nodes_ids:
                if node_id == id:
                    return True
                if node_id in visited:
                    continue
                visited.add(node_id)
                if checkIsLinked(self.nodes[node_id].neighbors, id):
                    return True
            return False
        return checkIsLinked(node.neighbors, b) or False

graph = Graph()
graph.addLink(1, 2)
graph.addLink(2, 3)
graph.addLink(1, 3)
graph.addLink(3, 4)
graph.addLink(5, 6)

graph.isLinked(1, 5)
graph.isLinked(1, 4)

graph.removeLink(1, 3)
graph.isLinked(1, 4)
