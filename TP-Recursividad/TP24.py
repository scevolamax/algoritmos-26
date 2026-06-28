# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from stack import Stack

personajes = [
    {"nombre": "Rocket Raccoon", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Black Widow", "peliculas": 6},
    {"nombre": "Captain America", "peliculas": 7},
    {"nombre": "Thor", "peliculas": 6},
    {"nombre": "Iron Man", "peliculas": 8}
]   
class Marvel:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas
    
    def __str__(self):
       return f'{self.nombre}, {self.peliculas}'

pila = Stack()
   
for mcu in personajes:
    pila.apilar(Marvel(mcu['nombre'], mcu['peliculas']))


# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

pos_groot = 0
pos_rocket = 0
pos = 1
paux = Stack()

while pila.size() > 0: 
    mcu = pila.desapilar()
    
    if mcu.nombre == 'Rocket Raccoon':
        pos_rocket = pos

    if mcu.nombre == 'Groot':
        pos_groot = pos
    
    paux.apilar(mcu)    
    pos += 1 
    
while paux.size() > 0:
    pila.apilar(paux.desapilar())
    
    
print('Rocket se encuentra en la posicion... ', pos_rocket)    
print('Groot se encuentra en la posicion... ', pos_groot)

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
print()
paux = Stack()

while pila.size() > 0:
    mcu = pila.desapilar()

    if mcu.peliculas > 5: 
        print(f'{mcu.nombre} participo en {mcu.peliculas} peliculas') 
    
    paux.apilar(mcu)

while paux.size() > 0: 
    pila.apilar(paux.desapilar())

print()
pila.show()