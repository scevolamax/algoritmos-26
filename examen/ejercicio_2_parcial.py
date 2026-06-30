# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:

# Listado ordenado de manera ascendente por nombre de los personajes.
# Determinar en que posicion esta The Thing y Rocket Raccoon.
# Listar todos los villanos de la lista.
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# Listar los superheores que comienzan con  Bl, G, My, y W.

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# Listado de superheroes ordenados por fecha de aparación.

# Modificar el nombre real de Ant Man a Scott Lang.
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue


class Marvel():
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
    
    def __str__(self):
        return f'{self.name} - {self.alias} - {self.real_name} - {self.short_bio} - {self.first_appearance} - {self.is_villain}'

def by_nom(item):
    return item.name
def by_realn(item):
    return item.real_name or ''
def by_aparicion(item):
    return item.first_appearance

l = List()
l.add_criterion('name', by_nom)
l.add_criterion('real_name', by_realn)
l.add_criterion('first_appearance', by_aparicion)

for hero in superheroes:
    l.append(Marvel(hero['name'], hero['alias'], hero['real_name'], hero['short_bio'], hero['first_appearance'], hero['is_villain']))



# Listado ordenado de manera ascendente por nombre de los personajes.
print('Listado ordenado de manera ascendente por nombre de los personajes:')
l.sort_by_criterion('name')
for p in l:
    print(p)
print()

# Determinar en que posicion esta The Thing y Rocket Raccoon.
for p in l:
    if p.name == 'The Thing':
        print(f'The Thing esta en la posicion: {l.index(p)}')
    elif p.name == 'Rocket Raccoon':
        print(f'Rocket Raccoon esta en la posicion: {l.index(p)}')
print()

# Listar todos los villanos de la lista.
print('Lista de villanos más buscados:  ')
for p in l:
    if p.is_villain:
        print(f'{p.name} - {p.is_villain}')
print()

# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
print('Villanos que aparecieron antes de 1980:  ')
villanos= Queue()
for p in l:
    if p.is_villain:
        villanos.arrive(p)
    
while villanos.size() > 0:
    taimados = villanos.attention()
    
    if taimados.first_appearance < 1980:
        print(taimados)
print()

# Listar los superheores que comienzan con  Bl, G, My, y W.
print('superheores que comienzan con  Bl, G, My, y W')
for p in l:
    if not p.is_villain and p.name.startswith(('Bl', 'G', 'My', 'W')):
        print(p)
print()

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
print('Listado ordenado de manera ascendente por nombre real de los personajes:')
l.sort_by_criterion('real_name')
for p in l:
    print(p)
print()


#Listado de superheroes ordenados por fecha de aparación.
print('Superheroes ordenados por fecha de aparición:')
l.sort_by_criterion('first_appearance')
for p in l:
    if not p.is_villain:
        print(f'{p.name} - {p.first_appearance}')
print()

# Modificar el nombre real de Ant Man a Scott Lang.
Ant_Man = l.search("Ant Man", 'name')
if Ant_Man is not None:
    l[Ant_Man].real_name = 'Scott Lang'
print()

# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print('Personajes que en su biografia incluyan la palabra time-traveling o suit: ')
#l.filter_contain_on_short_bio(['time-traveling', 'suit']) que esta mal?
for p in l:
    if p.short_bio is not None:
        bio = p.short_bio.lower()

        if 'time-traveling' in bio or 'suit' in bio:
            print(p)
print()

# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
eliminado = l.delete_value('Electro', 'name')
if eliminado is not None:
    print('Eliminando de la lista a ', eliminado) 

eliminado = l.delete_value('Baron Zemo', 'name')
if eliminado is not None:
    print('Eliminando de la lista a ', eliminado)    
print()


#l.show()
