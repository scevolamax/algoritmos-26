from criaturas_data import creatures
from tree import BinaryTree
from queue_ import Queue

arbol_criaturas = BinaryTree()

# Carga inicial del árbol (incluye la estructura de los puntos b y g)
for creature in creatures:
    arbol_criaturas.insert_node(creature['name'], other_value=creature)

# Punto a: listado inorden de las criaturas y quienes la derrotaron
print("--- PUNTO A: Listado inorden de criaturas y quiénes las derrotaron ---")
arbol_criaturas.inorden_creatures()

# Punto b: se debe permitir cargar una breve descripción sobre cada criatura
print("\n--- PUNTO B: Cargar una breve descripción sobre las criaturas ---")
arbol_criaturas.add_field("description", "")

descriptions_to_load = [
    ("Talos", "Autómata gigante de bronce que protegía a la isla de Creta."),
    ("Medusa", "Única Gorgona mortal, convertía en piedra a quienes la miraban a los ojos."),
    ("Cerbero", "Perro de tres cabezas que guardaba las puertas del Inframundo."),
]

for creature_name, desc in descriptions_to_load:
    node = arbol_criaturas.search(creature_name)
    if node is not None:
        node.other_values["description"] = desc
        print(f"Descripción cargada a {node.value}: {node.other_values['description']}")
    else:
        print(f"No se encontró la criatura {creature_name}")


# Punto c: mostrar toda la información de la criatura Talos
print("\n--- PUNTO C: Información de la criatura Talos ---")
node = arbol_criaturas.search("Talos")
if node is not None: #verificamos que no sea vacio (es una buena practica)
    print(f"Nombre: {node.value}")
    print(f"Derrotado por: {node.other_values['defeated_by'] or '-'}")
    print(f"Descripción: {node.other_values['description']}")
else:
    print("La criatura Talos no se encontró en el árbol.")



# Punto d: determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\n--- PUNTO D: Top 3 héroes o dioses que derrotaron más criaturas ---")
ranking = {}
arbol_criaturas.ranking_defeated(ranking) ## hacemos un inorden (aca lo llamamos ranking_defeated el cual ordena por derrotados) 

def order_by_defeated(item):
    return item[1] # Como cada elemento item es una tupla ('Heracles', 5), 
                   # item[0] es el nombre y item[1] es la cantidad. Esta función le dice a .sort() 
                   # que compare por el número (item[1]).

# Como un diccionario no tiene orden por valor entonces lo pasamos a una lista de tuplas para poder ordenarlo
ranking_list = list(ranking.items()) # ranking_list = list(ranking.items()) Convierte el diccionario en una lista de pares (héroe, cantidad)
ranking_list.sort(key=order_by_defeated, reverse=True)

for hero, count in ranking_list[:3]:
    print(f"{hero}: {count} criaturas derrotadas") # solamente show los primeros 3 elementos del ranking



### Punto e: listar las criaturas derrotadas por Heracles  ###
print("--- PUNTO E: Criaturas derrotadas por Heracles ---")
arbol_criaturas.inorden_defeated_by("Heracles")

### Punto f: listar las criaturas que no han sido derrotadas ###
print("--- PUNTO F: Criaturas que no han sido derrotadas ---")
arbol_criaturas.inorden_defeated_by(None)

### Punto g: además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturó ###
print("\n--- PUNTO G: Agregar el campo 'captured_by' a todos los nodos del árbol ---")
arbol_criaturas.add_field("captured_by", None)

### Punto h: modificar Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó ###
print("\n--- PUNTO H: Modificar criaturas capturadas por Heracles ---")
captured_creatures = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

for creature_name in captured_creatures:
    node = arbol_criaturas.search(creature_name)
    if node is not None:
        node.other_values["captured_by"] = "Heracles"
        print(f"{node.value} -> capturada por: {node.other_values['captured_by']}")
    else:
        print(f"No se encontró a {creature_name}")

### Punto i: se debe permitir búsquedas por coincidencia ###
print("\n--- PUNTO I: Búsqueda por coincidencia ---")
search_text = "Creta"
print(f"Criaturas que contienen '{search_text}':")
arbol_criaturas.proxy_search(search_text.lower())

### Punto j: eliminar al Basilisco y a las Sirenas ###
print("\n--- PUNTO J: Eliminar al Basilisco y a las Sirenas ---")
for creature_to_delete in ["Basilisco", "Sirenas"]:
    deleted_value, _  = arbol_criaturas.delete_node(creature_to_delete)
    if deleted_value is not None:
        print(f"Se eliminó del árbol a: {deleted_value}")
    else: 
        print(f"No se encontró a {creature_to_delete} para eliminar")

### Punto k: modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derrotó a varias ###
print("\n--- PUNTO K: Modificar Aves del Estínfalo ---")
node = arbol_criaturas.search("Aves del Estínfalo")
if node is not None:
    node.other_values["defeated_by"] = "Heracles (derrotó a varias)"
    print(f"Modificado: {node.value} derrotado por: {node.other_values['defeated_by']}")

### Punto l: modifique el nombre de la criatura Ladón por Dragón Ladón ###
print("\n--- PUNTO L: Modificar el nombre de Ladón por Dragón Ladón ---")
deleted_value, deleted_other_values = arbol_criaturas.delete_node("Ladón")  ## Lo eliminamos del árbol recuperando sus datos
if deleted_value is not None: ##Si existe actualizamos el nombre adentro de su diccionario:
    new_name = "Dragón Ladón" ## Modificamos el nombre de la criatura
    deleted_other_values["name"] = new_name 
    arbol_criaturas.insert_node(new_name, other_value=deleted_other_values) ## Insertamos el nodo con el nuevo nombre
    print(f"Se reemplazó '{deleted_value}' por '{new_name}'")

### Punto m: realizar un listado por nivel del árbol ###
print("--- PUNTO M: Listado por nivel del árbol ---")
arbol_criaturas.by_level()

### Punto n: muestre las criaturas capturadas por Heracles ###
print("--- PUNTO N: Criaturas capturadas por Heracles ---")
arbol_criaturas.inorden_captured_by("Heracles")

