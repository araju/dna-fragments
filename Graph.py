class Graph(object):
    """Represents a DAG with fast access for incoming and outgoing edges for each node."""
    def __init__(self):
        self.outgoingEdges = {}
        self.incomingEdges = {}

    def addEdge(self, fromNode, toNode):
        self.addToMap(fromNode, toNode, self.outgoingEdges)
        self.addToMap(toNode, fromNode, self.incomingEdges)

    def removeEdge(self, fromNode, toNode):
        self.removeFromMap(fromNode, toNode, self.outgoingEdges)
        self.removeFromMap(toNode, fromNode, self.incomingEdges)

    def getOutgoingEdges(self, fromNode):
        return self.outgoingEdges.get(fromNode, [])

    def getIncomingEdges(self, toNode):
        return self.incomingEdges.get(toNode, [])

    def hasEdges(self):
        return len(self.outgoingEdges) > 0

    def getNodesWithNoIncomingEdges(self):
        nodes = []
        for node in self.outgoingEdges:
            if node not in self.incomingEdges:
                nodes.append(node)
        return nodes

    def addToMap(self, key, value, dic):
        if key not in dic:
            dic[key] = []
        dic[key].append(value)

    def removeFromMap(self, key, value, dic):
        if key in dic:
            dic[key].remove(value)
            if len(dic[key]) == 0:
                dic.pop(key, None)
