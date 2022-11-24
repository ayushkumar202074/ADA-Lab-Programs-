def addEdge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v) 
    return adj

def graphColouring(adj, V):
    result = [-1] * V
    result[0] = 0

    available = [False] * V

    for i in range(1, V):
        for j in adj[i]:
            if (result[j] != -1):
                available[result[j]] = True

        colour = 0
        while colour < V:
            if (available[colour] == False):
                break
            colour += 1

        result[i] = colour 
        
        for j in adj[i]:
            if (result[j] != -1):
                available[result[j]] = False

    for i in range(V):
        print("Vertex", i, " --->  Color", result[i])


g1 = [[] for i in range(5)]
g1 = addEdge(g1, 0, 1)
g1 = addEdge(g1, 0, 2)
g1 = addEdge(g1, 1, 2)
g1 = addEdge(g1, 1, 3)
g1 = addEdge(g1, 2, 3)
g1 = addEdge(g1, 3, 4)
print("Coloring of graph 1 ")
graphColouring(g1, 5)

g2 = [[] for i in range(5)]
g2 = addEdge(g2, 0, 1)
g2 = addEdge(g2, 0, 2)
g2 = addEdge(g2, 1, 2)
g2 = addEdge(g2, 1, 4)
g2 = addEdge(g2, 2, 4)
g2 = addEdge(g2, 4, 3)
print("\nColoring of graph 2")
graphColouring(g2, 5)