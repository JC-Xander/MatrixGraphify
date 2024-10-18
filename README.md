```
███╗░░░███╗░█████╗░████████╗██████╗░██╗██╗░░██╗░██████╗░██████╗░░█████╗░██████╗░██╗░░██╗██╗███████╗██╗░░░██╗
████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░██║██║██╔════╝╚██╗░██╔╝
██╔████╔██║███████║░░░██║░░░██████╔╝██║░╚███╔╝░██║░░██╗░██████╔╝███████║██████╔╝███████║██║█████╗░░░╚████╔╝░
██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██╗██║░██╔██╗░██║░░╚██╗██╔══██╗██╔══██║██╔═══╝░██╔══██║██║██╔══╝░░░░╚██╔╝░░
██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║██║██╔╝╚██╗╚██████╔╝██║░░██║██║░░██║██║░░░░░██║░░██║██║██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
```

@author: 𓂀 𝒥-𝒳𝒶𝓃𝒹𝑒𝓇 𓂀<br>
@version: 0.0.1<br>
@since:  2024/10/18
@date: 2024/10/18

Convertir una matriz en un grafo el cual permita encontrar rutas tanto en diagonales como en verticales

# Funciones primarias
- Establecer un enum el cual indique un camino bloqueado por el cual no habra paso
- Bucar el camino mas corto de un punto A a un punto B representados por 2 coordenas (x,y)
    - Busqueda solo son los elemento horizontales
    - Busqueda solo con loe elementos verticales
    - Buscada con todos los elementos adyacentes
- Buscar el camino con menos peso si es una matriz con valores
- Buscar el camino mas corto(sin repetir)
- Buscar el camino mas largo(sin repetir)

# Estructuración
- Clase Node: Sera la clase que se conectara entre si para formar los enlaces del grafo esta podra tener un maximo de 8 conexiones. 4 en las diagonales 2 horizontales y 2 verticales
- Clase graf: Esta sera la encargada de realizar todas las conexiones correspondientes segun los datos en la matriz

