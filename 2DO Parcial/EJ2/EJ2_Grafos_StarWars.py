
from graph import Graph

g_star_wars = Graph(is_dir=False) # crea un grafo NO dirigido

# Cargar los personajes (vertices) con la cantidad total de episodios en other_values
personajes = [
    ("Luke Skywalker", 6),
    ("Darth Vader", 4),
    ("Yoda", 6),
    ("Boba Fett", 3),
    ("C3PO", 9),
    ("Leia", 6),
    ("Rey", 3),
    ("Kylo Ren", 3),
    ("Chewbacca", 7),
    ("Han Solo", 4),
    ("R2D2", 9),
    ("BB8", 3),
]

for nombre, episodios in personajes:
    g_star_wars.add_vertex(nombre, other_values=episodios)

# Cargar las aristas: (peso = episodios compartidos, origen, destino)
relaciones = [
    (9, "C3PO", "R2D2"),
    (6, "Luke Skywalker", "Leia"),
    (6, "Luke Skywalker", "C3PO"),
    (6, "Luke Skywalker", "R2D2"),
    (6, "Leia", "C3PO"),
    (6, "Leia", "R2D2"),
    (5, "Luke Skywalker", "Chewbacca"),
    (5, "Leia", "Chewbacca"),
    (5, "C3PO", "Chewbacca"),
    (5, "R2D2", "Chewbacca"),
    (4, "Han Solo", "Leia"),
    (4, "Han Solo", "Luke Skywalker"),
    (4, "Han Solo", "Chewbacca"),
    (4, "Han Solo", "C3PO"),
    (4, "Han Solo", "R2D2"),
    (3, "Luke Skywalker", "Darth Vader"),
    (3, "Luke Skywalker", "Yoda"),
    (3, "Darth Vader", "Leia"),
    (3, "Darth Vader", "C3PO"),
    (3, "Darth Vader", "R2D2"),
    (3, "Darth Vader", "Boba Fett"),
    (3, "Yoda", "C3PO"),
    (3, "Yoda", "R2D2"),
    (3, "Yoda", "Chewbacca"),
    (3, "Rey", "Kylo Ren"),
    (3, "Rey", "BB8"),
    (3, "Rey", "Chewbacca"),
    (3, "Rey", "C3PO"),
    (3, "Rey", "R2D2"),
    (2, "Rey", "Luke Skywalker"),
    (2, "Rey", "Leia"),
    (2, "Kylo Ren", "Leia"),
    (2, "Kylo Ren", "Luke Skywalker"),
    (2, "Kylo Ren", "BB8"),
    (2, "Boba Fett", "Han Solo"),
    (2, "Boba Fett", "Luke Skywalker"),
    (1, "Han Solo", "Rey"),
    (1, "Han Solo", "Kylo Ren"),
]

for peso, origen, destino in relaciones:
    g_star_wars.add_edge(peso, origen, destino)

# Hallar el arbol de expansion minimo desde el vertice que contiene a: C3PO, Yoda y Leia
print("--- ARBOL DE EXPANSION MINIMO (KRUSKAL) ---")
for personaje in ["C3PO", "Yoda", "Leia"]:
    min_tree = g_star_wars.kruskal(personaje)
    print(f"\nArbol de expansion minimo desde {personaje}:")
    peso_total = 0
    for edge in min_tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f"origin: {origin} -> destination: {destination} (weight: {weight})")
        peso_total += int(weight)
    print(f"Peso total: {peso_total}")

# Determinar cual es el numero maximo de episodios que comparten dos personajes e indicar los pares
print("--- MAXIMO DE EPISODIOS COMPARTIDOS ---")
max_episodios = 0
pares_maximos = []

for vertex in g_star_wars:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight
            pares_maximos = [(vertex.value, edge.destination)]
        elif edge.weight == max_episodios:
            # Evitamos duplicar el mismo par invertido (ej: R2D2-C3PO si ya esta C3PO-R2D2)
            if (edge.destination, vertex.value) not in pares_maximos:
                pares_maximos.append((vertex.value, edge.destination))

print(f"Numero maximo de episodios compartidos: {max_episodios}")
print("Pares de personajes que coinciden con ese numero:")
for p1, p2 in pares_maximos:
    print(f"  - {p1} y {p2}")

# Calcule el camino mas corto desde: C3PO a R2D2 y desde Yoda a Darth Vader
print("\n--- CAMINO MAS CORTO (DIJKSTRA) ---")
caminos_buscados = [
    ("C3PO", "R2D2"),
    ("Yoda", "Darth Vader"),
]

for origen, destino in caminos_buscados:
    if g_star_wars.exist_path(origen, destino):
        paths = g_star_wars.dijkstra(origen)
        destination = destino
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
        print(f"El camino mas corto desde {origen} hasta {destino} es: {' -> '.join(camino_completo)} con un costo de {peso_total}")
    else:
        print(f"No existe camino entre {origen} y {destino}")

# Indicar que personajes aparecieron en los nueve episodios de la saga
print("\n--- PERSONAJES QUE APARECIERON EN LOS 9 EPISODIOS ---")
for vertex in g_star_wars:
    if vertex.other_values == 9:
        print(f"  - {vertex.value} ({vertex.other_values} episodios)")


