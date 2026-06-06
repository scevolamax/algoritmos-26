# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el 
# nombre del personaje, el nombre del superhéroe y su género (Masculino M y FemeninoF) –
# por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc.,
# desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.


from queue_ import Queue
from marvel import Marvel

cola = Queue()

cola.arrivo(Marvel('Steve Rogers','Capitan America', 'M'))
cola.arrivo(Marvel('Natasha Romanoff','Black Widow', 'F'))
cola.arrivo(Marvel('Tony Stark', 'Iron Man', 'M'))
cola.arrivo(Marvel('Scott Lang','Ant-Man', 'M'))
cola.arrivo(Marvel('Wade Wilson','Deadpool', 'M'))
cola.arrivo(Marvel('Carol Danvers','Capitana Marvel', 'F'))
cola.arrivo(Marvel('Peter Parker', 'Spider-Man', 'M'))
cola.arrivo(Marvel('Bruce Banner','Hulk','M'))

### A) Mostrar nombre de capitana Marvel ###
for i in range(cola.size()):
    if cola.on_front().super == 'Capitana Marvel':
        print(f'Nombre de Capitana Marvel: ', cola.on_front().identidad)
    cola.move_to_end()
    
### B) mostrar los nombre de los superhéroes femeninos ###
print()
print('Superheroes Mujer:')
for i in range(cola.size()):
    if cola.on_front().genero == 'F':
        print(cola.on_front().super)
    cola.move_to_end()
    
### C) mostrar toda la banda ###
print()
print('Superheroes Hombre:')
for i in range(cola.size()):
    if cola.on_front().genero == 'M':
        print(cola.on_front().identidad)
    cola.move_to_end()
    

### Mostrar identidad de Ant Man ###
print()
for i in range(cola.size()):
    if cola.on_front().identidad == 'Scott Lang':
        print(f'Scott Lang es...', cola.on_front().super)
    cola.move_to_end()    

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
print('')

for i in range(cola.size()):
    personaje = cola.on_front()
    
    if personaje.identidad.startswith('S') or personaje.super.startswith('S'):
        print(f'Identidad: {personaje.identidad} | Super: {personaje.super} | Género: {personaje.genero}')
    cola.move_to_end()


### determinar si Carol Danvers se encuentra e indicar su superhéroe ###
print()

def cap_marvel(cola):
    if cola.size() == 0:
        return None

    super_carol = None

    for i in range(cola.size()):
        if cola.on_front().identidad == 'Carol Danvers':
            super_carol = cola.on_front().super
        cola.move_to_end()    
    
    return super_carol  

resultado = cap_marvel(cola)
    
if resultado:
    print('Carol Danvers se encuentra en los expedientes, ella es...', resultado )
else:
    print('Nadie en Shield coincide con ese nombre')



