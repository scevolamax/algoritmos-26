
from typing import Any, Optional

from queue_ import Queue
class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux


        node = __search(self.root, value)
        
        return node 
    
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def inorden(self) -> None:
        
        def __inorden(root):
            if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                __inorden(root.left)
            # print(f'procesa nodo actual')
            print(root.value, root.height)
            if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                __inorden(root.right)

        __inorden(self.root)
    
    def postorden(self) -> None:
        
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()

    def inorden_villain(self) -> None:
        
        def __inorden_villain(root):
            if root.left is not None:
                __inorden_villain(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)

    def postorden_hero(self):
    
        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if not root.other_values['is_villain']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:
        
        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> None:
        
        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)
            if prefix in root.value.lower():
                print(root.value)
            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)

    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if not root.other_values['is_villain']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count

### punto A ###
    def inorden_creatures(self) -> None:
        def __inorden_creatures(root):
            if root.left is not None:
                __inorden_creatures(root.left)
            print(f"Criatura: {root.value} | Derrotado por: {root.other_values['defeated_by'] or '-'}")
            if root.right is not None:
                __inorden_creatures(root.right)

        if self.root is not None:
            __inorden_creatures(self.root)

        #Siempre verificamos if self.root is not None: antes de llamar a la 
        #función recursiva, porque si el árbol estuviera vacío, intentar hacer root.left daría un error

### punto D ###
    def ranking_defeated(self, ranking_dict: dict) -> None:
        def __ranking_defeated(root, ranking_dict):
            if root.left is not None: 
                __ranking_defeated(root.left, ranking_dict)
            hero = root.other_values['defeated_by']
            if hero is not None: # es un filtro: si tienen 'None' no fueron derrotadas por nadie, y no se tiene que contar/ lo ignoramos
                if hero not in ranking_dict:
                    ranking_dict[hero] = 1  # Si el héroe no está en ranking_dict, lo inicializa en 1 (derroto a alguien).
                else:
                    ranking_dict[hero] += 1 # Si el héroe ya existe, le suma +1 a su contador (derroto a alguien mas).
            if root.right is not None:
                __ranking_defeated(root.right, ranking_dict)

        if self.root is not None:
            __ranking_defeated(self.root, ranking_dict)


# ranking_defeated(ranking) (Punto d): también hace un recorrido inorden, 
# pero en lugar de hacer print, va sumando +1 en un diccionario 
# ranking cada vez que encuentra un héroe en derrotado_por.

### puntos E y F ###
    def inorden_defeated_by(self, hero_name: Optional[str]) -> None:
        def __inorden_defeated_by(root, hero_name):
            if root.left is not None:
                __inorden_defeated_by(root.left, hero_name)
            if root.other_values['defeated_by'] == hero_name:
                print(root.value)
            if root.right is not None:
                __inorden_defeated_by(root.right, hero_name)

        if self.root is not None:
            __inorden_defeated_by(self.root, hero_name)

### punto G ###
# Recorre todo el arbol y a cada diccionario root.other_values 
# le inyecta el campo nuevo con su valor inicial.
    def add_field(self, field_name: str, default_value: Any = None) -> None:
        def __add_field(root, field_name, default_value):
            if root.left is not None:
                __add_field(root.left, field_name, default_value)
            root.other_values[field_name] = default_value
            if root.right is not None: 
                __add_field(root.right, field_name, default_value)

        if self.root is not None:
            __add_field(self.root, field_name, default_value)

### punto N ###
    def inorden_captured_by(self, hero_name: str) -> None:
        def __inorden_captured_by(root, hero_name):
            if root.left is not None:
                __inorden_captured_by(root.left, hero_name)
            if root.other_values.get('captured_by') == hero_name:
                print(root.value)
            if root.right is not None:
                __inorden_captured_by(root.right, hero_name)

        if self.root is not None:
            __inorden_captured_by(self.root, hero_name)

