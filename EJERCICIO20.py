
# Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.


class Pila:

    def __init__(self):
        self._datos = []

    def apilar(self, elemento):
        """Agrega un elemento en el tope de la pila."""
        self._datos.append(elemento)

    def desapilar(self):
        """Retira y retorna el elemento del tope. Lanza excepción si está vacía."""
        if self.esta_vacia():
            raise IndexError("No se puede desapilar: la pila está vacía.")
        return self._datos.pop()

    def tope(self):
        """Retorna el elemento del tope sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._datos[-1]

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamanio(self):
        return len(self._datos)

    def __str__(self):
        if self.esta_vacia():
            return "Pila vacía"
        lineas = ["╔══════════════════════╗"]
        for mov in reversed(self._datos):
            lineas.append(f"║  {str(mov):<20}║")
        lineas.append("╚══════════════════════╝")
        return "\n".join(lineas)



class Movimiento:

    DIRECCIONES_VALIDAS = {
        "N":  "Norte",
        "S":  "Sur",
        "E":  "Este",
        "O":  "Oeste",
        "NE": "Noreste",
        "NO": "Noroeste",
        "SE": "Sureste",
        "SO": "Suroeste",
    }
    OPUESTOS = {
        "N":  "S",
        "S":  "N",
        "E":  "O",
        "O":  "E",
        "NE": "SO",
        "SO": "NE",
        "NO": "SE",
        "SE": "NO",
    }

    def __init__(self, pasos: int, direccion: str):
        direccion = direccion.upper().strip()
        if direccion not in self.DIRECCIONES_VALIDAS:
            raise ValueError(
                f"Dirección '{direccion}' no válida. "
                f"Use: {', '.join(self.DIRECCIONES_VALIDAS.keys())}"
            )
        if pasos <= 0:
            raise ValueError("La cantidad de pasos debe ser un entero positivo.")
        self.pasos = pasos
        self.direccion = direccion

    def invertir(self):
        """Retorna un nuevo Movimiento con la dirección opuesta."""
        return Movimiento(self.pasos, self.OPUESTOS[self.direccion])

    def __str__(self):
        nombre = self.DIRECCIONES_VALIDAS[self.direccion]
        return f"{self.pasos:>3} paso(s) → {nombre}"



class Robot:

    def __init__(self, nombre: str = "R2D2"):
        self.nombre = nombre
        self._pila_movimientos = Pila()   # historial
        self._pila_retorno = Pila()       # secuencia de regreso (se llena al calcular)

    def mover(self, pasos: int, direccion: str):
        mov = Movimiento(pasos, direccion)
        self._pila_movimientos.apilar(mov)
        print(f"  [+] Movimiento registrado: {mov}")

    def registrar_secuencia(self, movimientos: list[tuple]):
        print(f"\n{'═'*50}")
        print(f"  Registrando secuencia para el robot '{self.nombre}'")
        print(f"{'═'*50}")
        for pasos, direccion in movimientos:
            self.mover(pasos, direccion)


    def mostrar_historial(self):
        """Muestra todos los movimientos registrados (de base a tope)."""
        print(f"\n   Historial de movimientos — Robot '{self.nombre}'")
        print(f"  (Base = primer movimiento │ Tope = último movimiento)\n")
        print(self._pila_movimientos)


    def calcular_retorno(self):
        """
        Desapila el historial, invierte cada movimiento y apila en
        una segunda pila que representa la ruta de regreso.
        El historial original se reconstruye al terminar.
        """
        if self._pila_movimientos.esta_vacia():
            print("  ⚠  No hay movimientos registrados.")
            return

        # Pila auxiliar para reconstruir el historial
        pila_aux = Pila()
        self._pila_retorno = Pila()

        # Vaciamos historial → aux (invierte orden) y llenamos retorno
        while not self._pila_movimientos.esta_vacia():
            mov = self._pila_movimientos.desapilar()
            pila_aux.apilar(mov)
            self._pila_retorno.apilar(mov.invertir())

        # Restauramos el historial original desde aux
        while not pila_aux.esta_vacia():
            self._pila_movimientos.apilar(pila_aux.desapilar())

    def mostrar_retorno(self):
        """Muestra la secuencia de retorno calculada."""
        self.calcular_retorno()

        print(f"\n  Secuencia de RETORNO — Robot '{self.nombre}'")
        print(f"  (Orden de ejecución: de arriba hacia abajo)\n")

        if self._pila_retorno.esta_vacia():
            print("  Sin movimientos de retorno.")
            return

        # Copiamos la pila de retorno a una lista para mostrarla en orden
        pila_tmp = Pila()
        pasos_retorno = []

        while not self._pila_retorno.esta_vacia():
            mov = self._pila_retorno.desapilar()
            pasos_retorno.append(mov)
            pila_tmp.apilar(mov)

        # Restauramos la pila de retorno
        while not pila_tmp.esta_vacia():
            self._pila_retorno.apilar(pila_tmp.desapilar())

        print(f"  {'N°':<5} {'Pasos':<8} {'Dirección'}")
        print(f"  {'─'*35}")
        for i, mov in enumerate(pasos_retorno, 1):
            nombre_dir = Movimiento.DIRECCIONES_VALIDAS[mov.direccion]
            print(f"  {i:<5} {mov.pasos:<8} {nombre_dir}")
        print(f"  {'─'*35}")
        print(f"  Total de movimientos: {len(pasos_retorno)}")

    def ejecutar_retorno(self):
        """
        Simula la ejecución del retorno desapilando uno a uno
        los movimientos de la pila de retorno.
        """
        self.calcular_retorno()

        if self._pila_retorno.esta_vacia():
            print("  Sin movimientos para ejecutar.")
            return

        print(f"\n  Ejecutando retorno paso a paso...\n")
        paso_num = 1
        while not self._pila_retorno.esta_vacia():
            mov = self._pila_retorno.desapilar()
            nombre_dir = Movimiento.DIRECCIONES_VALIDAS[mov.direccion]
            print(f"  Paso {paso_num:>2}: {mov.pasos} paso(s) hacia el {nombre_dir}")
            paso_num += 1

        print(f"\n  Robot '{self.nombre}' ha regresado al punto de partida.")



def menu_interactivo():
    """Permite ingresar movimientos por consola."""
    print("\n" + "═"*50)
    print("        CONTROL DE ROBOT CON PILA")
    print("═"*50)
    nombre = input("  Nombre del robot (Enter = R2D2): ").strip() or "R2D2"
    robot = Robot(nombre)

    while True:
        print(f"\n  {'─'*40}")
        print("  1. Registrar movimiento")
        print("  2. Ver historial")
        print("  3. Ver secuencia de retorno")
        print("  4. Ejecutar retorno (paso a paso)")
        print("  5. Salir")
        print(f"  {'─'*40}")
        opcion = input("  Opción: ").strip()

        if opcion == "1":
            try:
                pasos = int(input("  Cantidad de pasos: "))
                print("  Direcciones: N  S  E  O  NE  NO  SE  SO")
                direccion = input("  Dirección: ").strip()
                robot.mover(pasos, direccion)
            except (ValueError, IndexError) as e:
                print(f"  Error: {e}")

        elif opcion == "2":
            robot.mostrar_historial()

        elif opcion == "3":
            robot.mostrar_retorno()

        elif opcion == "4":
            robot.ejecutar_retorno()

        elif opcion == "5":
            print("   Chau.\n")
            break
        else:
            print("  Opción no válida.")



def demo():
    print("\n" + "═"*50)
    print("         DEMO — ROBOT CON PILA")
    print("═"*50)

    robot = Robot("Wall-E")

    # Secuencia de ejemplo
    secuencia = [
        (3,  "N"),
        (5,  "NE"),
        (2,  "E"),
        (4,  "SE"),
        (1,  "S"),
        (6,  "SO"),
        (3,  "O"),
        (2,  "NO"),
    ]

    robot.registrar_secuencia(secuencia)
    robot.mostrar_historial()
    robot.mostrar_retorno()
    robot.ejecutar_retorno()

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--interactivo":
        menu_interactivo()
    else:
        demo()
        print("\n" + "─"*50)
        print("     ejecutá con --interactivo para modo manual")
        print("     python robot_pila.py --interactivo")
