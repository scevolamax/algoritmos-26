# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from super_heroes_data import superheroes
from tree import BinaryTree


class MarvelCharacter():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"
    


arbol_marvel = BinaryTree()
print(f'cantidad de elementos {len(superheroes)}')

#A En cada nodo ya tiene si es villano o no, por lo que ya esta implementado el campo booleano.
for marvel_character in superheroes:
    arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

#B listar los villanos ordenados alfabéticamente;
arbol_marvel.inorden_villain()
print()

#C superhéroes que empiezan con W
print('superhéroes que empiezan con W')
arbol_marvel.inorden_hero_star_with('W')
print()

#D determinar cuántos superhéroes hay el árbol;
print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')
print()

# E Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
search_str = input('ingrese lo que quiere buscar (str): ')
arbol_marvel.proxy_search(search_str.lower())

search_str = input('ingrese lo que quiere modificar (Dr Strannnnnge --> Dr Strange): ')

node = arbol_marvel.search(search_str)
if node is not None:
    new_name = input('ingrese el nuevo nombre: ')
    delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
    delete_other_value['name'] = new_name
    arbol_marvel.insert_node(new_name, delete_other_value)

print()
arbol_marvel.inorden_hero_star_with('D')
print()

#F listado ordenados de manera descendente;
arbol_marvel.postorden_hero()
print()

#G 2 arboles --> 1.heroes y 2.villanos  
arbol_villanos = BinaryTree()
arbol_heroes = BinaryTree()

arbol_marvel.heroes_o_villain(arbol_heroes, arbol_villanos)

# I. determinar cuántos nodos tiene cada árbol;
print(f'Cantidad de nodos en árbol de villanos: {arbol_villanos.count_nodes()}')
print(f'Cantidad de nodos en árbol de héroes: {arbol_heroes.count_nodes()}')
print()


# II. realizar un barrido ordenado alfabéticamente de cada árbol.
arbol_villanos.inorden()
print()
arbol_heroes.inorden()
print()