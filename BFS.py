class Graph:
    def __init__(self, edges=None):
        if edges is None:
            edges = []
        self.edges = edges

    def getVertices(self):
        vertices = set()
        for edge in self.edges:
            vertices.update(edge)
        return list(vertices)

    def BFS(self, initialState, goalState):
        frontier = [initialState]
        explored = []
        while frontier:
            state = frontier.pop(0)
            explored.append(state)
            if state == goalState:
                return explored
            for edge in self.edges:
                if state in edge:
                    neighbor = edge[1] if edge[0] == state else edge[0]
                    if neighbor not in explored and neighbor not in frontier:
                        frontier.append(neighbor)
        return False


if __name__ == '__main__':
    graph_elements = [
        ("a", "b"), ("a", "c"),
        ("b", "d"), ("b", "e"),
        ("c", "f"), ("c", "g"),
        ("d", "h"), ("d", "i"),
        ("e", "j"), ("e", "k"),
        ("f", "l"), ("f", "m"),
        ("g", "n"), ("g", "o"),
        ("h", ""), ("i", ""),
        ("j", ""), ("k", ""),
        ("l", ""), ("m", ""),
        ("n", ""), ("o", "")
    ]
    graph1 = Graph(graph_elements)
    result = graph1.BFS("a", "d")
    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
        print(s)
    else:
        print('No path exists')