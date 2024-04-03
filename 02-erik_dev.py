"""
/*
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# Función sin parámetros ni retorno


def mi_funcion():
    print("Hola Mundo")


mi_funcion()

# Funcion con uno o varios parámetros


def mi_funcion2(param1, param2):
    print(param1, param2)


mi_funcion2("Hola", "Mundo")

# Función con retorno


def mi_funcion3(param1, param2):
    return param1 + param2


resultado = mi_funcion3(2, 3)
print(resultado)

# Función dentro de función


def mi_funcion4(param1):
    def funcion_dentro(param2):
        return param2 + 1
    return funcion_dentro(param1)


resultado2 = mi_funcion4(2)
print(resultado2)

# Funciones del lenguaje
print(len("Hola Mundo"))
print(type(2))
print("Mouredev".upper())

# Función con variable global y local
global_var = 10


def mi_funcion5(param1):
    local_var = 5
    return param1 + local_var + global_var


resultado3 = mi_funcion5(2)
print(resultado3)
# print(local_var) # Error, local_var no está definida en este ámbito

# EXTRA


def extr(texto1, texto2):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 5 == 0:
            print(texto2)

        elif i % 3 == 0:
            print(texto1)
        else:
            print(i)


resultado_extra = extr("Erik", "Dev")
print(resultado_extra)
