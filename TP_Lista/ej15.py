# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, 
# cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. 
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. 
# Se pide resolver las siguientes actividades utilizando lista de lista 
# implementando las funciones necesarias:


# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from list_ import List

class Pokemon(): ## lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
    def __init__(self, nom, nivel, tipo, subtipo):
        self.nombre = nom
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'Nombre: {self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo} | Subtipo: {self.subtipo}'

class Entrenador(): ##se conoce nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. 
    def __init__(self, nom, tor_ganados, derrotas, victorias):
        self.nombre = nom
        self.tor_ganados = tor_ganados
        self.derrotas = derrotas
        self.victorias = victorias 
    
    
    # Lista de listas: Usamos la clase List para los pokémons de cada entrenador
        self.pokemons = List()
        # Añadimos los criterios de búsqueda para la clase List interna
        self.pokemons.add_criterion('nombre', lambda p: p.nombre)
        self.pokemons.add_criterion('nivel', lambda p: p.nivel)
    
    
    def __str__(self):
        return f'Nombre: {self.nombre} | Torneos ganados: {self.tor_ganados} | Derrotas: {self.derrotas} | Victorias: {self.victorias}'

#2_Definir criterios de ordenamiento
def by_nombre(item):
    return item.nombre

def by_torneos(item):
    return item.torneos_ganados

l = List() #3_creo la lista de entrenadores
l.add_criterion('nombre', by_nombre)
l.add_criterion('torneos', by_torneos)
   
#4_ cargo los datos y ahí recien empiezo 
# Creando entrenadores
e1 = Entrenador("Ash", 4, 20, 150)
e2 = Entrenador("Misty", 2, 40, 60)
e3 = Entrenador("Brock", 1, 30, 70)
e4 = Entrenador("Cynthia", 10, 5, 200)
e5 = Entrenador("", 3, 10, 50)

# Asignando Pokémons a Ash
e1.pokemons.append(Pokemon("Pikachu", 50, "Eléctrico", "Ninguno"))
e1.pokemons.append(Pokemon("Charizard", 65, "Fuego", "Volador"))
e1.pokemons.append(Pokemon("Wingull", 20, "Agua", "Volador"))

# Asignando Pokémons a Misty
e2.pokemons.append(Pokemon("Starmie", 45, "Agua", "Psíquico"))
e2.pokemons.append(Pokemon("Gyarados", 60, "Agua", "Volador"))

# Asignando Pokémons a Brock (Pokémons repetidos)
e3.pokemons.append(Pokemon("Geodude", 30, "Roca", "Tierra"))
e3.pokemons.append(Pokemon("Geodude", 32, "Roca", "Tierra"))
e3.pokemons.append(Pokemon("Onix", 40, "Roca", "Tierra"))

# Asignando Pokémons a Cynthia
e4.pokemons.append(Pokemon("Garchomp", 88, "Dragón", "Tierra"))
e4.pokemons.append(Pokemon("Lucario", 75, "Lucha", "Acero"))
e4.pokemons.append(Pokemon("Terrakion", 70, "Roca", "Lucha"))

# Asignando Pokémons a Ramos
e5.pokemons.append(Pokemon("Scovillain", 45, "Fuego", "Planta"))
e5.pokemons.append(Pokemon("Tyrantrum", 55, "Roca", "Dragón"))

# Agregando entrenadores a la lista principal
l.append(e1)
l.append(e2)
l.append(e3)
l.append(e4)
l.append(e5)

# a. obtener la cantidad de Pokémons de un determinado entrenador;
print("a. Cantidad de Pokémons de Ash:")
pos = l.search("Ash", "nombre")
if pos is not None:
    print(f'Ash tiene {l[pos].pokemons.size()} Pokémons.')
else:
    print('No se encontró al entrenador.')
print()

# b. listar los entrenadores que hayan ganado más de tres torneos;
print("b. Entrenadores con más de tres torneos ganados:")
for e in l:
    if e.tor_ganados > 3:
        print(e.nombre)
print()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print("c. Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados:")
max_torneos = -1
entrenador_top = None

for e in l:
    if e.tor_ganados > max_torneos:
        max_torneos = e.tor_ganados 
        entrenador_top = e
        
if entrenador_top is not None and entrenador_top.pokemons.size() > 0:
    max_nivel = -1
    pokemon_top = None
    for p in entrenador_top.pokemons:
        if p.nivel > max_nivel:
            max_nivel = p.nivel
            pokemon_top = p
    print(f'{entrenador_top.nombre} tiene a {pokemon_top.nombre} (Nivel: {pokemon_top.nivel})')
print()
          
# d. mostrar todos los datos de un entrenador y sus Pokémos;
print("d. Datos de Misty y sus Pokemon:")
pos = l.search('Misty', 'nombre')

if pos is not None: 
    print(l[pos])
    l[pos].pokemons.show()
print()

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

for e in l:
    total = e.derrotas + e.victorias
    if total > 0:
        porcentaje = (e.victorias / total) * 100
        if porcentaje > 79:
            print(f'{e.nombre} ({porcentaje:.2f}%)')
print()


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print("f. Entrenadores con Pokémons Fuego/Planta o Agua/Volador:")
for e in l:
    for p in e.pokemons:
        if (p.tipo == "Fuego" and p.subtipo == "Planta") or (p.tipo == "Agua" and p.subtipo == "Volador"):
            print(f'{e.nombre} tiene a {p.nombre}')
print() 


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print("g. Promedio de nivel de los Pokémons de Brock:")
pos = l.search("Brock", "nombre")
if pos is not None:
    suma = 0
    cantidad = l[pos].pokemons.size()
    for p in l[pos].pokemons:
        suma += p.nivel
    if cantidad > 0:
        print(f'Promedio de nivel: {suma / cantidad}')
print()


# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print("h. Cuantos entrenadores tienen a 'Pikachu':")
contador = 0
for e in l:
    if e.pokemons.search("Pikachu", "nombre"):
        contador += 1

if contador > 1: 
    print(f'{contador} entrenadores tienen a Pikachu.')
elif contador == 1:
    print(f'{contador} solo entrenador tienen a Pikachu.')
else:
    print('Ninún entrenador tiene a Pikachu') 
print()

# i. mostrar los entrenadores que tienen Pokémons repetidos;
print("i. Entrenadores con Pokémons repetidos:")
for e in l:
    nombres = []
    tiene_repetido = False
    
    for p in e.pokemons:
        if p.nombre in nombres:
            tiene_repetido = True
        nombres.append(p.nombre)
    
    if tiene_repetido:
        print(e.nombre)
print()

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
print("j. Entrenadores con Tyrantrum, Terrakion o Wingull:")
buscados = ["Tyrantrum", "Terrakion", "Wingull"]
for e in l:
    for p in e.pokemons:
        if p.nombre in buscados:
            print(f'{e.nombre} tiene a {p.nombre}')
print()



print("k. Determinar si un entrenador X tiene al Pokémon Y:")
x = input("Ingrese entrenador: (Ash, Misty, Brock, Cynthia, Ramos) ")
y = input("Ingrese Pokemon buscado: (primer letra en mayusculas porfa jaja) ")


# K.
pos_e = l.search(x, 'nombre')
if pos_e is not None:
    entrenador = l[pos_e]
    pos_p = entrenador.pokemons.search(y, 'nombre')

    if pos_p is not None:
        print(f'¡Encontrado!\n{entrenador}\n{entrenador.pokemons[pos_p]}')
    else:
        print(f'El entrenador {x} no tiene a {y}.')
        
else:
    print(f'El entrenador {x} no existe en la lista.')
print()