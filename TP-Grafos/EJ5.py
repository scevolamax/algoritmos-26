# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos necesarios
# para resolver las tareas, listadas a continuación:
#       a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor,
#          router, switch, impresora;
#       b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
#          Red Hat, Debian, Arch;
#       c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
#          Red Hat, Fedora hasta la impresora;
#       d. encontrar el árbol de expansión mínima;
#       e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
#       f. indicar desde que computadora del switch 01 es el camino más corto
#          al servidor “MongoDB”;
#       g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
#       h. debe utilizar un grafo no dirigido.

from list_ import List
from queue_ import Queue
from stack import Stack
from heap import HeapMin
from graph import Graph

# h. Grafo no dirigido
g = Graph(is_dir=False)

# a. Carga de nodos con su nombre (value) y su tipo (other_values)

g.add_vertex('Ubuntu', 'pc')
g.add_vertex('Mint', 'pc')
g.add_vertex('Manjaro', 'pc')
g.add_vertex('Fedora', 'pc')
g.add_vertex('Parrot', 'pc')
g.add_vertex('Red Hat', 'notebook')
g.add_vertex('Debian', 'notebook')
g.add_vertex('Arch', 'notebook')
g.add_vertex('Impresora', 'impresora')
g.add_vertex('Guarani', 'servidor')
g.add_vertex('MongoDB', 'servidor')
g.add_vertex('Switch 1', 'switch')
g.add_vertex('Switch 2', 'switch')
g.add_vertex('Router 1', 'router')
g.add_vertex('Router 2', 'router')
g.add_vertex('Router 3', 'router')

# Carga de aristas segun el esquema de red
# Conexiones de Switch 1
g.add_edge(17, 'Debian', 'Switch 1')
g.add_edge(18, 'Ubuntu', 'Switch 1')
g.add_edge(22, 'Impresora', 'Switch 1')
g.add_edge(80, 'Mint', 'Switch 1')
g.add_edge(29, 'Switch 1', 'Router 1')

# Conexiones entre Routers
g.add_edge(37, 'Router 1', 'Router 2')
g.add_edge(43, 'Router 1', 'Router 3')
g.add_edge(50, 'Router 2', 'Router 3')

# Conexiones de Router 2
g.add_edge(25, 'Red Hat', 'Router 2')
g.add_edge(9, 'Guarani', 'Router 2')

# Conexion de Router 3 a Switch 2
g.add_edge(61, 'Router 3', 'Switch 2')

# Conexiones de Switch 2
g.add_edge(40, 'Manjaro', 'Switch 2')
g.add_edge(12, 'Parrot', 'Switch 2')
g.add_edge(5, 'MongoDB', 'Switch 2')
g.add_edge(56, 'Arch', 'Switch 2')
g.add_edge(3, 'Fedora', 'Switch 2')

# b. Barrido en profundidad y amplitud desde las tres notebooks: Red Hat, Debian, Arch
notebooks = ['Red Hat', 'Debian', 'Arch']

for nb in notebooks:
    print(f'--- Barrido en profundidad (DFS) desde {nb} ---')
    g.deep_show(nb)
    print(f'--- Barrido en amplitud (BFS) desde {nb} ---')
    g.amplitude_show(nb)
    print()

# otra forma para el B
# print("Barrido en amplitud partiendo desde Red Hat: ") 
# Grafo.amplitude_show("Red Hat")
# print()
# print("Barrido en amplitud partiendo desde Debian: ")
# Grafo.amplitude_show("Debian")
# print()
# print("Barrido en amplitud partiendo desde Arch: ") 
# Grafo.amplitude_show("Arch")
# print()

# print("Barrido en profundidad partiendo desde Red Hat: ") 
# Grafo.deep_show("Red Hat")
# print()
# print("Barrido en profundidad partiendo desde Debian: ") 
# Grafo.deep_show("Debian")
# print()
# print("Barrido en profundidad partiendo desde Arch: ") 
# Grafo.deep_show("Arch")
# print()



# c. Camino mas corto desde Manjaro, Red Hat, Fedora hasta Impresora
equipos_impresion = ['Manjaro', 'Red Hat', 'Fedora']

for equipo in equipos_impresion:
    exist_path = g.exist_path(equipo, 'Impresora')
    if exist_path:
        paths = g.dijkstra(equipo)
        destination = 'Impresora'
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
        print(f'Desde {equipo} hasta Impresora: {" -> ".join(camino_completo)} (costo: {peso_total})')


# d. Arbol de expansion minima (Kruskal)
print()
min_tree = g.kruskal('Ubuntu')

print(min_tree)
peso_total = 0
for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    print(f'origin {origin} destination {destination}')
    peso_total += int(weight)
print(f'peso total del arbol de expansion minima: {peso_total}')

# e. Determinar desde que pc (no notebook) es el camino mas corto hasta el servidor "Guarani"
print()
menor_costo_guarani = None
mejor_pc_guarani = None
mejor_camino_guarani = []

for vertex in g:
    if vertex.other_values == 'pc':
        paths = g.dijkstra(vertex.value)
        destination = 'Guarani'
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

        if menor_costo_guarani is None or peso_total < menor_costo_guarani:
            menor_costo_guarani = peso_total
            mejor_pc_guarani = vertex.value
            mejor_camino_guarani = camino_completo

print(f'La PC con el camino mas corto a Guarani es {mejor_pc_guarani}: {" -> ".join(mejor_camino_guarani)} (costo: {menor_costo_guarani})')

# f. Indicar desde que computadora del Switch 1 es el camino mas corto al servidor "MongoDB"
print()
pos_switch1 = g.search('Switch 1', 'value')
menor_costo_mongo = None
mejor_compu_mongo = None
mejor_camino_mongo = []

if pos_switch1 is not None:
    for edge in g[pos_switch1].edges:
        pos_vecino = g.search(edge.destination, 'value')
        vecino = g[pos_vecino]
        if vecino.other_values in ['pc', 'notebook']:
            paths = g.dijkstra(vecino.value)
            destination = 'MongoDB'
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

            if menor_costo_mongo is None or peso_total < menor_costo_mongo:
                menor_costo_mongo = peso_total
                mejor_compu_mongo = vecino.value
                mejor_camino_mongo = camino_completo

print(f'La computadora del Switch 1 con camino mas corto a MongoDB es {mejor_compu_mongo}: {" -> ".join(mejor_camino_mongo)} (costo: {menor_costo_mongo})')

# g. Cambiar la conexion de la impresora al Router 2 y volver a resolver el punto b
print()
g.delete_edge('Impresora', 'Switch 1')
g.add_edge(22, 'Impresora', 'Router 2')

for nb in notebooks:
    print(f'--- [Nuevo] Barrido en profundidad (DFS) desde {nb} ---')
    g.deep_show(nb)
    print(f'--- [Nuevo] Barrido en amplitud (BFS) desde {nb} ---')
    g.amplitude_show(nb)
    print()


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

