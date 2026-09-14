# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:


# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.


#1_defino la clase y sus atributos

from list_ import List

class Superheroe(): #conocemos:  nom, ano, casa, bio ### la clase solo define los atributos y comportamientos, pero no entiende de objetos
    def __init__(self, nom, ano, casa, bio): # el self solo llama los elementos de clase 
        self.nom = nom
        self.ano = ano
        self.casa = casa
        self.bio = bio
        
    def __str__(self): ### estructura para mostrar mas lindos los datos
        return f'Nombre: {self.nom} | Año de aparición: {self.ano} | Casa: {self.casa} | Biografía: {self.bio}'

#2_Definir criterios de ordenamiento
#o sea, lo ordeno por anio, por nombre
def by_nombre(item):
    return item.nom

def by_lanzamiento(item):
    return item.ano

def by_editorial(item):
    return item.casa

def by_biografia(item):
    return item.bio

#3_creo lista y cargar los criterios
#los criterios ordenan la lista segun un criterio especifico(ej, por nombre)
l = List()
l.add_criterion('nombre', by_nombre)
l.add_criterion('lanzamiento', by_lanzamiento)
l.add_criterion('editorial', by_editorial)
l.add_criterion('biografia', by_biografia)

#4_ cargo los datos y ahí recien empzamos
l.append(Superheroe("Linterna Verde", 1940, "DC", "Heroe con anillo de poder y traje verde"))
l.append(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium"))
l.append(Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo de las artes místicas"))
l.append(Superheroe("Flash", 1940, "DC", "Velocista escarlata"))
l.append(Superheroe("Star-Lord", 1976, "Marvel", "Líder de Guardianes de la Galaxia"))
l.append(Superheroe("Batman", 1939, "DC", "Vigilante con armadura tecnológica"))
l.append(Superheroe("Superman", 1938, "DC", "Kryptoniano con traje azul y capa roja"))  
l.append(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona"))
l.append(Superheroe("Capitana Marvel", 1968, "Marvel", "Heroína cósmica"))
l.append(Superheroe("Moon Knight", 1975, "Marvel", "Justiciero con múltiples personalidades"))
print()

# a. eliminar el nodo que contiene la información de Linterna Verde;
print(f'dato eliminado:{l.delete_value("Linterna Verde", "nombre")}') # llamamos nuestra lista (l), busco borrar el valor "Linterna Verde", y lo busco usando el criterio del nombre 
#print(f'dato eliminado: {l.delete_value("Linterna Verde",criterion="nombre")}')  --> otra forma de escribirlo
print()

# b. mostrar el año de aparición de Wolverine;
wolverine = l.search("Wolverine", "nombre") # obtengo el indice de la posición de wolverine, y luego accedo a su atributo lanzamiento para mostrarlo.
if wolverine is not None:
    print(f'El año de aparición de Wolverine es: {l[wolverine].ano}')
else: 
    print('Wolverine no se encuentra en la lista') 
print()
#print(f'El año de aparición de Wolverine es: {l.search("Wolverine", "nombre").ano}') 




# c. cambiar la casa de Dr. Strange a Marvel;
pos = l.search("Dr. Strange", "nombre") 
if pos is not None: # if pos: --> otra forma de escribirlo
    l[pos].casa = "Marvel" 
print()

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print("Superhéroes que mencionan 'traje' o 'armadura' en su biografía: ")
for i in range(l.size()): 
    if 'traje' in l[i].bio or 'armadura' in l[i].bio:
        print(f' {l[i].nom}')
print()

#e) Mostrar nombre y casa de los héroes anteriores a 1963
print("Superhéroe con fecha de aparición anterior a 1963: ") 
for heroe in l:
    if heroe.ano < 1963:
        print(heroe.nom)
print()

# for i in range(l.size()):
#     if l[i].ano < 1963:
#         print(f'{l[i].nom} - {l[i].casa}') #
# print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
for n in ['Capitana Marvel', 'Mujer Maravilla']:
    pos = l.search(n, "nombre")
    if pos is not None:
        print(f'{n} pertenece a la casa: {l[pos].casa}')
    
    
# g. mostrar toda la información de Flash y Star-Lord;
for nombre in ['Flash', 'Star-Lord']:
    pos = l.search(nombre, 'nombre')
    if pos is not None:
        print(f'Expediente de: {l[pos]}')

print()
# h. listar los superhéroes que comienzan con la letra B, M y S;
print("Superhéroes que comienzan con B, M o S:")

for heroe in l:
    if heroe.nom.startswith(('B', 'M', 'S')):
        print(heroe.nom) 

# for i in range(l.size()):
#     if (l[i].nom[0] == "B" or l[i].nom[0] == "M" or l[i].nom[0] == "S"):
#         print(l[i].nom)

print()
# i. determinar cuántos superhéroes hay de cada casa de comic.
dc = 0
marvel = 0

for publisher in l:

    if publisher.casa == 'DC':
        dc += 1
    if publisher.casa == 'Marvel':
       marvel += 1
        
print(f'Cantidad por casa:')
print('Marvel:', marvel)
print('DC:', dc)

# print()
# l.show()
