"""
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""

s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))  # Hala

# División
print(s2.split("t"))  # ["Py","hon"]

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("erik dev".title())
print("erik dev".capitalize())

# Eliminación de espacios al principio y al final
print(" erik dev ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Erik Caceres @erikdev"

# Búsqueda de posición
print(s3.find("erik"))
print(s3.find("Erik"))
print(s3.find("E"))
print(s3.lower().find("R"))

# Búsqueda de ocurrencias
print(s3.lower().count("e"))

# Formateo
print("Saludo: {}, lenguje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

# Palindromos


def palindromo(palabra):

    palabra_unida = palabra.replace(" ", "").lower()
    if palabra_unida == palabra_unida[::-1]:
        print("Es palindromo")
    else:
        print("No es palindromo")


palindromo("Anita lava la Tina")

# Anagramas


def anagrama(word_1, word_2):
    if sorted(word_1) == sorted(word_2):
        print("Es anagrama")
    else:
        print("No es anagrama")


anagrama("palabra", "brapala")

# Isogramas


def isograma(word):
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            print("No es isograma")
            break
    else:
        print("Es isograma")


isograma("escritura")  # No es isograma
isograma("murcielago")  # Es isograma
