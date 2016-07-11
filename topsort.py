def topsort(graph):
    sortedList = []
    noIncomingEdges = graph.getNodesWithNoIncomingEdges()
    while len(noIncomingEdges) > 0:
        if len(noIncomingEdges) > 1:
            print "Warning: there may be more than one way to construct this sequence"
        n = noIncomingEdges.pop(0)
        sortedList.append(n)
        for m in graph.getOutgoingEdges(n):
            graph.removeEdge(n,m)
            if len(graph.getIncomingEdges(m)) == 0:
                noIncomingEdges.append(m)
    if graph.hasEdges():
        raise Exception('There is a cycle in our graph!')
    return sortedList
