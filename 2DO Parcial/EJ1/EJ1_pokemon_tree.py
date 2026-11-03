from pokemon_data import pokemons
from tree import BinaryTree

# los tres arboles (indices: nombre, numero y tipo)
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], other_value=pokemon)
    arbol_numero.insert_node(pokemon['numero'], other_value=pokemon)
    for tipo in pokemon['tipo']:
        arbol_tipo.insert_node(tipo, other_value=pokemon)
print()

# Mostrar todos los datos de un Pokemon a partir de su numero y nombre (por proximidad)
numero_buscado = 25
nodo_numero = arbol_numero.search(numero_buscado)
if nodo_numero is not None:
    print(f"Datos del Pokemon N° {numero_buscado}:")
    print(nodo_numero.other_values)
else:
    print(f"No se encontro el Pokemon N° {numero_buscado}")

print()
search_text = "bul"
print(f"Pokemons que contienen '{search_text}':")
arbol_nombre.proxy_search(search_text.lower())
print()  

# Mostrar todos los nombres de los Pokemons de tipo: fantasma, fuego, acero y electrico
tipos_buscados = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos_buscados:
    print(f"Pokemon de tipo {tipo}:")
    arbol_tipo.inorden_tipo(tipo)
    print()

# listado en orden ascendente por numero y nombre de Pokemon, y listado por nivel por nombre
print("Listado en orden ascendente por numero:")
arbol_numero.inorden()
print()

print("Listado en orden ascendente por nombre:")
arbol_nombre.inorden()
print()

print("Listado por nivel por nombre:")
arbol_nombre.by_level()
print()

# Mostrar todos los Pokemons que son debiles frente a Jolteon, Lycanroc y Tyrantrum
atacantes = ["Jolteon", "Lycanroc", "Tyrantrum"]
for nombre_atacante in atacantes:
    nodo_atacante = arbol_nombre.search(nombre_atacante)
    if nodo_atacante is not None:
        tipos_atacante = nodo_atacante.other_values['tipo']
        print(f"Pokemons debiles frente a {nombre_atacante} (tipo {tipos_atacante}):")
        arbol_nombre.inorden_debilidad(tipos_atacante)
        print()

# Mostrar todos los tipos de Pokemons y cuantos hay de cada tipo
print("Cantidad de Pokemons por cada tipo:")
conteo_por_tipo = arbol_tipo.contar_tipos()
for tipo, cantidad in conteo_por_tipo.items():
    print(f"{tipo}: {cantidad}")
print()

# Determinar cuantos Pokemons tienen megaevolucion
print(f"Cantidad de Pokemons con megaevolucion: {arbol_nombre.contar_mega_evolucion()}")

# Determinar cuantos Pokemons tienen forma gigamax
print(f"Cantidad de Pokemons con forma gigamax: {arbol_nombre.contar_gigamax()}")








