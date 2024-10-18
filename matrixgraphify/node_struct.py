from enum import Enum

# Enum to represent the cardinal directions
class Direction(Enum):
    """
    Enum para representar las direcciones cardinales junto con sus coordenadas en un plano 2D.
    Las direcciones incluyen:
    - NO (Noroeste) 
    - N (Norte)
    - NE (Noreste)
    - E (Este)
    - SE (Sureste)
    - S (Sur)
    - SO (Suroeste)
    - O (Oeste)
    El segundo valor de cada dirección es una tupla que representa su desplazamiento en un plano donde el origen son las corrdenas del nodo padre (0,0).
    donde el primer valor indica su desplazamiento horizontal y el segundo su desplazamiento vertical.
    | (-1,-1) | (0,-1) | (1,-1) |
    | (-1,0)  | (0,0)  | (1,0)  |
    | (-1,1)  | (0,1)  | (1,1)  |
    """
    NO = (0,(-1,-1))
    N = (1,(0,-1))
    NE = (2,(1,-1))
    E = (3,(1,0))
    SE = (4,(1,1))
    S = (5,(0,1))
    SO = (6,(-1,1))
    O = (7,(-1,0))

    @property
    def cardinal(self) -> int:
        """Devuelve la posicion donde se encuentra el nodo en la lista de vertices del nodo padre"""
        return self.value[0]
    
    @property
    def coordenate(self) -> tuple:
        """Devuelve las coordenadas del nodo en un plano"""
        return self.value[1]


class Node:
    """Clase que representa un nodo en el grafo, almacena su valor, peso y conexiones"""
    # Constructor
    def __init__(self, value = None, peso:int = 0):
        """Inicializa un nuevo nodo con su valor, peso y con todos sus vertices vacios"""
        self.value = value
        
        # No se puede crear un nodo con vertices ya definidos estos solo se pueden añadir mediante el metodo add_vertex
        # sera un implementacion futura
        if isinstance(peso, int) == False:
            raise ValueError('Peso must be an integer')
        
        # Si el value del nodo es un entero y no se le asignado un peso se tomar el value como peso
        if peso == 0 and isinstance(value, int) == True:
            peso = value    

        self.peso = peso
        self.vertex = [
                ('NO', None),
                ('N', None),
                ('NE', None),
                ('E', None),
                ('SE', None),
                ('S', None),
                ('SO', None),
                ('O', None),
            ]

    # Sustituya la conexion en la direccion especificada
    def add_vertex(self, direction:Direction = None, node:'Node' = None) -> bool:
        """Añade una conexión a un nodo en la direccion especificada, si el nodo ya cuenta con un vertice en esa direccion este sera reemplazado"""
        if direction is None:
            raise ValueError('Direction is required')
        
        if not isinstance(node, Node):
            raise ValueError('Node is required')
        
        self.vertex[direction.cardinal] = (direction, node)
        return True

    # Retorna un iterador
    def get_vertex_adjacent(self) -> iter:
        """Devuelve un iterador con los nodos adyacentes al nodo padre"""
        return (self.vertex[i] for i in range(1, len(self.vertex), 2))
    
    def get_vertex_perpendicular(self) -> iter:
        """Devuelve un iterador con los nodos perpendiculares al nodo padre"""
        return (self.vertex[i] for i in range(0, len(self.vertex), 2))
    
    def get_vertex(self, direction:Direction) -> 'Node':
        """Devuelve el nodo en la direccion especificada"""
        return self.vertex[direction.cardinal][1]
    
    def all_vertex(self) -> iter:
        """Devuelve un iterador con todos los nodos conectados al nodo padre"""
        return self.vertex.__iter__()
        
    def __str__(self) -> str:
        """Devuelve la representación en string del nodo"""
        return str(self.value)