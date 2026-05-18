
#  Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G

class Pila:

    def __init__(self):
        self._datos = []

    def apilar(self, elemento):
        self._datos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._datos.pop()

    def tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._datos[-1]

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamanio(self):
        return len(self._datos)

class Personaje:
    def __init__(self, nombre: str, peliculas: int):
        self.nombre    = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre:<30} │ Películas: {self.peliculas}"


def _copiar_pila(pila: Pila) -> Pila:
    """Devuelve una copia de la pila sin alterar la original."""
    aux  = Pila()
    copia = Pila()

    while not pila.esta_vacia():
        aux.apilar(pila.desapilar())

    while not aux.esta_vacia():
        elem = aux.desapilar()
        pila.apilar(elem)
        copia.apilar(elem)

    aux2 = Pila()
    while not copia.esta_vacia():
        aux2.apilar(copia.desapilar())
    return aux2          # mismo orden que la original


def a_posicion_personajes(pila: Pila, buscar: list[str]) -> dict:
    objetivos   = {n.lower(): None for n in buscar}
    encontrados = 0
    total       = len(objetivos)

    tmp      = Pila()
    posicion = 1

    while not pila.esta_vacia() and encontrados < total:
        p = pila.desapilar()
        tmp.apilar(p)
        if p.nombre.lower() in objetivos and objetivos[p.nombre.lower()] is None:
            objetivos[p.nombre.lower()] = posicion
            encontrados += 1
        posicion += 1

    while not pila.esta_vacia():
        tmp.apilar(pila.desapilar())

    while not tmp.esta_vacia():
        pila.apilar(tmp.desapilar())

    resultado = {}
    for nombre in buscar:
        pos = objetivos.get(nombre.lower())
        resultado[nombre] = pos
    return resultado

#  ACTIVIDAD B 

def b_mas_de_cinco_peliculas(pila: Pila) -> list[Personaje]:
    copia      = _copiar_pila(pila)
    resultado  = []

    while not copia.esta_vacia():
        p = copia.desapilar()
        if p.peliculas > 5:
            resultado.append(p)

    return resultado

#  ACTIVIDAD C 
def c_peliculas_viuda_negra(pila: Pila) -> int | None:
    nombres_objetivo = {"black widow", "viuda negra"}
    copia    = _copiar_pila(pila)
    resultado = None

    while not copia.esta_vacia():
        p = copia.desapilar()
        if p.nombre.lower() in nombres_objetivo:
            resultado = p.peliculas
            break

    return resultado


#  ACTIVIDAD D 
def d_nombres_CDG(pila: Pila) -> list[Personaje]:
    letras    = {"c", "d", "g"}
    copia     = _copiar_pila(pila)
    resultado = []

    while not copia.esta_vacia():
        p = copia.desapilar()
        if p.nombre.strip()[0].lower() in letras:
            resultado.append(p)

    return resultado


#  HELPERS DE PRESENTACIÓN

SEP   = "─" * 52
SEP2  = "═" * 52

def titulo(texto: str):
    print(f"\n{SEP2}")
    print(f"  {texto}")
    print(SEP2)

def subtitulo(texto: str):
    print(f"\n  {texto}")
    print(f"  {SEP}")

def mostrar_lista(personajes: list[Personaje]):
    if not personajes:
        print("  (ninguno)")
        return
    for i, p in enumerate(personajes, 1):
        print(f"  {i:>2}. {p}")

def mostrar_pila_completa(pila: Pila):

    copia = _copiar_pila(pila)
    print(f"\n  {'POS':<5} {'NOMBRE':<30} {'PELÍCULAS'}")
    print(f"  {SEP}")
    pos = 1
    while not copia.esta_vacia():
        p = copia.desapilar()
        marcador = "◄ CIMA" if pos == 1 else ""
        print(f"  {pos:<5} {p.nombre:<30} {p.peliculas:<10} {marcador}")
        pos += 1
    print(f"  {SEP}")


# ══════════════════════════════════════════════════════════
#  DATOS MCU
# ══════════════════════════════════════════════════════════
PERSONAJES_MCU = [
    # (nombre,                    películas)
    ("Iron Man",                       10),
    ("Captain America",                 7),
    ("Thor",                            8),
    ("Black Widow",                     7),
    ("Hulk",                            7),
    ("Hawkeye",                         6),
    ("Nick Fury",                       9),
    ("Doctor Strange",                  5),
    ("Spider-Man",                      6),
    ("Black Panther",                   4),
    ("Captain Marvel",                  4),
    ("Scarlet Witch",                   5),
    ("Vision",                          4),
    ("Falcon",                          5),
    ("War Machine",                     6),
    ("Ant-Man",                         4),
    ("Wasp",                            3),
    ("Groot",                           5),
    ("Rocket Raccoon",                  5),
    ("Star-Lord",                       4),
    ("Gamora",                          4),
    ("Drax",                            4),
    ("Nebula",                          5),
    ("Mantis",                          4),
    ("Loki",                            7),
    ("Thanos",                          5),
    ("Shang-Chi",                       2),
    ("Eternals",                        1),
    ("Daredevil",                       3),
    ("Ghost Rider",                     1),
]


def construir_pila() -> Pila:
    """
    Apila los personajes en orden de la lista:
    el último de la lista queda en la cima.
    """
    pila = Pila()
    for nombre, peliculas in PERSONAJES_MCU:
        pila.apilar(Personaje(nombre, peliculas))
    return pila

#  MAIN

def main():
    pila = construir_pila()

    titulo("PILA DE PERSONAJES MCU")
    mostrar_pila_completa(pila)

    # ── Actividad A ─────────────────────────────────────
    subtitulo("A) Posición de Rocket Raccoon y Groot")
    buscar = ["Rocket Raccoon", "Groot"]
    posiciones = a_posicion_personajes(pila, buscar)
    for nombre, pos in posiciones.items():
        if pos is not None:
            print(f"  • {nombre:<20} → posición {pos}")
        else:
            print(f"  • {nombre:<20} → no encontrado en la pila")

    # ── Actividad B ─────────────────────────────────────
    subtitulo("B) Personajes con más de 5 películas")
    mas5 = b_mas_de_cinco_peliculas(pila)
    mostrar_lista(mas5)
    print(f"\n  Total encontrados: {len(mas5)}")

    # ── Actividad C ─────────────────────────────────────
    subtitulo("C) Películas de la Viuda Negra (Black Widow)")
    cant = c_peliculas_viuda_negra(pila)
    if cant is not None:
        print(f"  Black Widow participó en {cant} película(s) del MCU.")
    else:
        print("  Black Widow no se encuentra en la pila.")

    # ── Actividad D ─────────────────────────────────────
    subtitulo("D) Personajes cuyo nombre empieza con C, D o G")
    cdg = d_nombres_CDG(pila)
    mostrar_lista(cdg)
    print(f"\n  Total encontrados: {len(cdg)}")

    print(f"\n{SEP2}\n")


if __name__ == "__main__":
    main()
