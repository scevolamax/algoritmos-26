# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
#     tareas:
#       a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#          baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#       b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
#          es la distancia entre los ambientes, se debe cargar en metros;
#       c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#          para conectar todos los ambientes;
#       d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#          determinar cuántos metros de cable de red se necesitan para conectar el router con el
#          Smart Tv.

from list_ import List
from queue_ import Queue
from stack import Stack
from heap import HeapMin
from graph import Graph

g = Graph(is_dir=False)

# a. Carga de vertices (ambientes de la casa)
g.add_vertex('cocina')
g.add_vertex('comedor')
g.add_vertex('cochera')
g.add_vertex('quincho')
g.add_vertex('baño 1')
g.add_vertex('baño 2')
g.add_vertex('habitación 1')
g.add_vertex('habitación 2')
g.add_vertex('sala de estar')
g.add_vertex('terraza')
g.add_vertex('patio')

# b. Carga de aristas (al menos 3 por vertice, y 2 vertices con 5 aristas: cocina y quincho)
# Cocina (5 aristas)
g.add_edge(3, 'cocina', 'comedor')
g.add_edge(32, 'cocina', 'cochera')
g.add_edge(19, 'cocina', 'quincho')
g.add_edge(5, 'cocina', 'habitación 2')
g.add_edge(8, 'cocina', 'terraza')

# Quincho (completa 5 aristas: ya tiene cocina, sumamos 4 mas)
g.add_edge(22, 'quincho', 'habitación 1')
g.add_edge(14, 'quincho', 'terraza')
g.add_edge(13, 'quincho', 'baño 2')
g.add_edge(18, 'quincho', 'baño 1')

# Resto de ambientes (completan al menos 3 aristas cada uno)
g.add_edge(2, 'comedor', 'baño 1')
g.add_edge(1, 'comedor', 'patio')
g.add_edge(4, 'baño 2', 'comedor')
g.add_edge(15, 'cochera', 'sala de estar')
g.add_edge(9, 'cochera', 'baño 2')
g.add_edge(24, 'habitación 1', 'terraza')
g.add_edge(29, 'habitación 1', 'patio')
g.add_edge(21, 'habitación 2', 'sala de estar')
g.add_edge(6, 'habitación 2', 'patio')
g.add_edge(11, 'baño 1', 'sala de estar')

# c. Arbol de expansion minima y metros de cable necesarios para conectar todos los ambientes
print()
min_tree = g.kruskal('cocina')

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination} ({weight}m)')
    peso_total += int(weight)
print(f'Metros totales de cable para conectar todos los ambientes: {peso_total}m')

# d. Camino mas corto desde habitacion 1 hasta sala de estar
print()
exist_path = g.exist_path('habitación 1', 'sala de estar')

if exist_path:
    paths = g.dijkstra('habitación 1')

    destination = 'sala de estar'
    peso_total = None
    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    camino_completo.reverse()
    print(f'El camino mas corto es: {" -> ".join(camino_completo)} y requiere {peso_total}m de cable de red')


