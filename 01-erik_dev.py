"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
# OPERADORES ARITMETICOS
suma = 5 + 5
resta = 5 - 5
multiplicacion = 5 * 5
division = 5 / 5
division_entera = 5 // 5
modulo = 5 % 5
potencia = 5 ** 5
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo)
print(potencia)

# OPERADOR DE COMPARACION
igual = 5 == 5
distinto = 5 != 5
mayor_que = 5 > 5
menor_que = 5 < 5
mayor_o_igual_que = 5 >= 5
menor_o_igual_que = 5 <= 5
print(igual)
print(distinto)
print(mayor_que)
print(menor_que)
print(mayor_o_igual_que)
print(menor_o_igual_que)

# OPERADORES LOGICOS

# and = True si ambos son True
# or = True si alguno es True
# not = True si es False
and_op = True and True
or_op = True or False
not_op = not False
print(and_op)
print(or_op)
print(not_op)

# OPERADORES DE ASIGNACION
x = 5
x += 5
x -= 5
x *= 5
x /= 5
x %= 5
x //= 5
x **= 5
print(x)

# OPERADORES DE IDENTIDAD
x = 5
y = 5
z = 6
is_op = x is y
is_not_op = x is not z
print(is_op)
print(is_not_op)

# OPERADORES DE PERTENENCIA
lista = [1, 2, 3, 4, 5]
pertenece = 1 in lista
no_pertenece = 6 not in lista
print(pertenece)
print(no_pertenece)

print(f"'o' in 'hola' = {'o' in 'hola'}")
print(f"'o' in 'hola' = {'o' not in 'hola'}")


# OPERADORES DE BITS

# & = AND
# | = OR
# ^ = XOR
# ~ = NOT
# << = Desplazamiento a la izquierda
# >> = Desplazamiento a la derecha

x = 5  # 5 = 101 en binario
y = 6  # 6 = 110 en binario
and_bit = x & y
or_bit = x | y
xor_bit = x ^ y
not_bit = ~x
desplazamiento_izquierda = x << 1
desplazamiento_derecha = x >> 1
print(and_bit)  # 101 & 110 = 100 = 4
print(or_bit)  # 101 | 110 = 111 = 7
print(xor_bit)  # 101 ^ 110 = 011 = 3
print(not_bit)  # ~101 = 010 = 2
print(desplazamiento_izquierda)  # 101 << 1 = 1010 = 10
print(desplazamiento_derecha)  # 101 >> 1 = 10 = 2

# ESTRUCTURAS DE CONTROL
# CONDICIONALES

# Se cumple la condicion del if

my_string = "erik"

if my_string == "erik":
    print("my_string es igual a erik")
elif my_string == "erik2":
    print("my_string es igual a erik2")
else:
    print("my_string no es igual a erik ni a erik2")

# ITERATIVAS

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# EXCEPCIONES
try:
    print(10 / 1)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Se ejecuta siempre")

# EJERCICIO EXTRA
for i in range(10, 55):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
