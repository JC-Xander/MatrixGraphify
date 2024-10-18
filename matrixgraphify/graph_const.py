from .node_struct import Direction, Node
import copy

class Graph:
    def __init__(self, matrix):
        self.node_matrix = self._convert_matrix_Node(matrix)
        self._connect_nodes()

    def _convert_matrix_Node(self, matrix:list) -> list:
        """Convierte los elemetos de la matriz en nodos"""
        matrix_copy = copy.deepcopy(matrix)

        for i in range(len(matrix_copy)):
            for j in range(len(matrix_copy[i])):
                current = matrix_copy[i][j]
                if isinstance(current, tuple) and len(current) == 2:
                    matrix_copy[i][j] = Node(current, int(current[1]))
                else:
                    matrix_copy[i][j] = Node(current)

        return matrix_copy
    
    def _connect_nodes(self):
        """Conecta los nodos en la matriz"""
        for y, row in enumerate(self.node_matrix):
            for x, current in enumerate(row):
                punto = (x, y)
                for direc in Direction:
                    conect_posicion = tuple(map(sum, zip(punto, direc.coordenate)))
                    if (0 <= conect_posicion[0] < len(row)) and (0 <= conect_posicion[1] < len(self.node_matrix)):
                        connect_node = self.node_matrix[conect_posicion[1]][conect_posicion[0]]
                        current.add_vertex(direc, connect_node)

    def get_node(self, x:int, y:int) -> Node:
        """Devuelve un nodo en la posicion especificada"""
        return self.node_matrix[y][x]

        