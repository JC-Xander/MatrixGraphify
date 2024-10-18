from matrixgraphify import Graph


matriz = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

grafo = Graph(matriz)

nodo = grafo.get_node(1, 1)
print(nodo)
for children in nodo.all_vertex():
    print(children[1])

