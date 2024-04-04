"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto
en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización
y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más
de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.
"""
# Creación de estructuras de datos

# Listas
# Creación de una lista vacía
lista_vacia = []
# Creación de una lista con elementos
lista_con_elementos = [1, 2, 3, 4, 5]
# Inserción de un elemento al final de la lista
lista_con_elementos.append(6)
# Inserción de un elemento en una posición específica
lista_con_elementos.insert(2, 7)
print(lista_con_elementos)
# Borrado de un elemento por valor
lista_con_elementos.remove(7)
print(lista_con_elementos)
# Borrado de un elemento por posición
del lista_con_elementos[0]
# Actualización de un elemento
lista_con_elementos[0] = 8
print(lista_con_elementos)
# Ordenación de la lista
lista_con_elementos.sort()
print(lista_con_elementos)
# Inversión de la lista
lista_con_elementos.reverse()
print(lista_con_elementos)
# Búsqueda de un elemento
print(8 in lista_con_elementos)  # True
print(9 in lista_con_elementos)  # False
# Longitud de la lista
print(len(lista_con_elementos))  # 5
# Acceso a un elemento por posición
print(lista_con_elementos[0])  # 8
# Acceso a un rango de elementos
print(lista_con_elementos[1:3])  # [6, 5]
# Acceso a un rango de elementos con saltos
print(lista_con_elementos[::2])  # [8, 5, 3]
# Acceso a un rango de elementos con saltos y en orden inverso
print(lista_con_elementos[::-1])  # [3, 4, 5, 6, 8]
# Acceso a un rango de elementos con saltos y en orden inverso
print(lista_con_elementos[::-2])  # [3, 5, 8]
# Acceso a un rango de elementos con saltos y en orden inverso
print(lista_con_elementos[::-3])  # [3, 6]
# Acceso a un rango de elementos con saltos y en orden inverso
print(lista_con_elementos[::-4])  # [3, 8]
# Acceso a un rango de elementos con saltos y en orden inverso
print(lista_con_elementos[::-5])  # [3]

# Tuplas
# Creación de una tupla vacía
tupla_vacia = ()
# Creación de una tupla con elementos
tupla_con_elementos = (1, 2, 3, 4, 5)
# Acceso a un elemento por posición
print(tupla_con_elementos[0])  # 1
# Acceso a un rango de elementos
print(tupla_con_elementos[1:3])  # (2, 3)
# Acceso a un rango de elementos con saltos
print(tupla_con_elementos[::2])  # (1, 3, 5)
# Acceso a un rango de elementos con saltos y en orden inverso
print(tupla_con_elementos[::-1])  # (5, 4, 3, 2, 1)

# Diccionarios
# Creación de un diccionario vacío
diccionario_vacio = {}
# Creación de un diccionario con elementos
diccionario_con_elementos = {'nombre': 'Erik', 'edad': 25, 'pais': 'Chile'}
# Inserción de un elemento
diccionario_con_elementos['ciudad'] = 'Santiago'
print(diccionario_con_elementos)
# Borrado de un elemento por clave
del diccionario_con_elementos['pais']
print(diccionario_con_elementos)
# Actualización de un elemento
diccionario_con_elementos['edad'] = 26
print(diccionario_con_elementos)
# Acceso a un elemento por clave
print(diccionario_con_elementos['nombre'])  # Erik
# Acceso a un elemento por clave con get
print(diccionario_con_elementos.get('edad'))  # 26
# Acceso a todas las claves
# dict_keys(['nombre', 'edad', 'ciudad'])
# dict_keys(['nombre', 'edad', 'ciudad'])
print(diccionario_con_elementos.keys())
# Acceso a todos los valores
# dict_values(['Erik', 26, 'Santiago'])
print(diccionario_con_elementos.values())
# Acceso a todas las claves y valores
# dict_items([('nombre', 'Erik'), ('edad', 26), ('ciudad', 'Santiago')])
print(diccionario_con_elementos.items())
# Búsqueda de una clave
print('nombre' in diccionario_con_elementos)  # True
print('pais' in diccionario_con_elementos)  # False
# Longitud del diccionario
print(len(diccionario_con_elementos))  # 3
# Borrado de todos los elementos
diccionario_con_elementos.clear()
print(diccionario_con_elementos)  # {}
# Copia de un diccionario
diccionario_copia = diccionario_con_elementos.copy()
print(diccionario_copia)  # {}
# Creación de un diccionario con claves y valores por defecto
diccionario_con_default = dict(nombre='Erik', edad=25, pais='Chile')
print(diccionario_con_default)
# Actualización de un diccionario con otro
diccionario_con_default.update({'ciudad': 'Santiago'})
print(diccionario_con_default)
# Borrado de un elemento por clave con pop
diccionario_con_default.pop('edad')
print(diccionario_con_default)
# Borrado de un elemento por posición con popitem
diccionario_con_default.popitem()
print(diccionario_con_default)
# Borrado de un elemento por clave con pop
diccionario_con_default.pop('nombre')

# Sets
# Creación de un Set vacío
conjunto_vacio = set()
# Creación de un Set con elementos
conjunto_con_elementos = {1, 2, 3, 4, 5}
# Inserción de un elemento
conjunto_con_elementos.add(6)
print(conjunto_con_elementos)
# Borrado de un elemento
conjunto_con_elementos.remove(6)
print(conjunto_con_elementos)
# Búsqueda de un elemento
print(1 in conjunto_con_elementos)  # True
print(6 in conjunto_con_elementos)  # False
# Longitud del Set
print(len(conjunto_con_elementos))  # 5
# Borrado de todos los elementos
conjunto_con_elementos.clear()
print(conjunto_con_elementos)  # set()
# Creación de un Set con una lista
conjunto_con_lista = set([1, 2, 3, 4, 5])
print(conjunto_con_lista)
# Creación de un Set con una tupla
conjunto_con_tupla = set((1, 2, 3, 4, 5))
print(conjunto_con_tupla)
# Creación de un Set con un diccionario
conjunto_con_diccionario = set({'nombre': 'Erik', 'edad': 25})
print(conjunto_con_diccionario)  # {'nombre', 'edad'} # Solo las claves
# Creación de un Set con un string
conjunto_con_string = set('Erik')
print(conjunto_con_string)

# Agenda de contactos


def my_agenda():
    agenda = {}

    def insertar_contacto():
        telefono = input("Ingresa el teléfono del contacto: ")
        if telefono.isdigit() and len(telefono) == 11:
            agenda[nombre] = telefono
        else:
            print("Número de teléfono inválido.")

    while True:
        print("""
        1.- Buscar contacto
        2.- Insertar contacto
        3.- Actualizar contacto
        4.- Eliminar contacto
        5.- Salir
        """)
        opcion = input("¿Qué operación deseas realizar? ")
        if opcion == '1':
            nombre = input("Ingresa el nombre del contacto: ")
            if nombre in agenda:
                print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
            else:
                print("El contacto no existe.")
        elif opcion == '2':
            nombre = input("Ingresa el nombre del contacto: ")
            insertar_contacto()
        elif opcion == '3':
            nombre = input("Ingresa el nombre del contacto: ")
            if nombre in agenda:
                insertar_contacto()
            else:
                print("El contacto no existe.")
        elif opcion == '4':
            nombre = input("Ingresa el nombre del contacto: ")
            if nombre in agenda:
                del agenda[nombre]
            else:
                print("El contacto no existe.")
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")


my_agenda()
