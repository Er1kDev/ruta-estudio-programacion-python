"""
EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""
# www.python.org
# Comentario de una línea

"""
Esto es 
un comentario 
tambien
"""

'''
Esto tambien es
otra forma de hacer 
comentarios
'''

# DATOS PRIMITIVOS

# Variable
my_variable = "Hola"
my_variable = "Nuevo valor de la variable"

# No se puede reasignar una constante
MY_CONSTANT = "Soy una constante"
MY_CONSTANT = "No se puede reasignar"

# Numeros Enteros
my_int = 5

# Numeros Flotantes o decimales
my_float = 5.5

# Booleanos
my_bool = True
my_bool = False

# Cadena de texto
my_string = "Hola Mundo"
my_other_string = 'Hola Mundo'

# Imprimir por terminal
print("¡Hola, Python!")

# Imprimir el tipo de dato de las variables
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
