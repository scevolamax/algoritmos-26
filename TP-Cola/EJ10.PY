# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra
# ‘Python’, si perder datos en la cola;

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre
# las 11:43 y las 15:57, y determinar cuántas son.


from queue_ import  Queue
from mensajes import Mensaje 
from stack import Stack

cola = Queue()

cola.arrivo(Mensaje("Facebook", "Nuevo comentario", "10:30"))
cola.arrivo(Mensaje("Twitter", "Aprendiendo Python", "12:15"))
cola.arrivo(Mensaje("Instagram", "Te etiquetaron", "14:20"))
cola.arrivo(Mensaje("Twitter", "Python es genial", "15:10"))

### A) eliminar notificaciones facebook ###
for i in range(cola.size()):
    if cola.on_front().app == 'Facebook':
        cola.atencion() # lo elimina
    else:
        cola.move_to_end() # los conserva

### B) twits con la palabra phyton, sin eliminar ###
for i in range(cola.size()):
      notificacion = cola.on_front()
      if cola.on_front().app == 'Twitter' and  'Python' in cola.on_front().msj:
          print()
          print(f'Notificación encontrada: {cola.on_front().time} - {cola.on_front().msj}')
      cola.move_to_end()

# for i in range(cola.size()):
#     notificacion = cola.on_front()
#     if notificacion.app == 'Twitter' and  'Python' in notificacion.msj:
#         print(f'Notificación encontrada: {notificacion.time} - {notificacion.msj}')
#     cola.move_to_end()
    
### C) usar una pila, almacenar noti y show notificaciones, de entre las 11:43 y las 15:57 ###
pila_aux = Stack()
for i in range(cola.size()):
    if cola.on_front().time >= '11:43' and cola.on_front().time <= '15:57': 
        pila_aux.apilar(cola.on_front())
    cola.move_to_end()

print()
print("Notificaciones entre las 11:43 y las 15:57")
print()
pila_aux.show() 
print(f'Cantidad de notificaciones en ese horario: {pila_aux.size()}')


