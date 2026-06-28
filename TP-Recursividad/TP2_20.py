# Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.


from stack import Stack
#los datos que guarda son cantidad de pasos y dirección –norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–
movimientos = [
    {"pasos": 5, "direccion": "norte"},
    {"pasos": 3, "direccion": "este"},
    {"pasos": 2, "direccion": "sur"},
    {"pasos": 4, "direccion": "oeste"},
    {"pasos": 1, "direccion": "noreste"},
    {"pasos": 2, "direccion": "suroeste"},
    {"pasos": 3, "direccion": "sureste"}
]

opuestas ={
    "norte": "sur", 
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

pila = Stack()

class Robot(): 
    def __init__(self, pasos, direccion):
        self.direccion = direccion
        self.pasos = pasos     
        
    def __str__(self):
        return f'{self.pasos} - {self.direccion}'

for moves in movimientos:
    pila.apilar(Robot(moves['pasos'], moves['direccion']))

# genere secuencia de movimientos para hacer volver al robot a su lugar de partida, por el mismo camino que fue.
paux = Stack()
while pila.size() > 0: 
    move = pila.desapilar()
    
    if move is not None:
        print(f'El robot se movio {move.pasos} pasos hacia {move.direccion}')
        paux.apilar(move)

while paux.size() > 0:
    pila.apilar(paux.desapilar())

print(f'El robot llego a destino')
print()
print("Camino de regreso...")


while pila.size() > 0:
    movimiento = pila.desapilar()
    print(f"{movimiento.pasos} pasos hacia {opuestas[movimiento.direccion]}")
