# -*- coding: utf-8 -*-
import math
"""
Editor de Spyder

Este es un archivo temporal.
"""
# comentario de linea
"""
 comentario de parrafo
"""

# Hola mundo
print("hola mundo")

# Variables

x = 4  # int
y = "Texto"  # string
z = 4.5  # float
a = True  # boolean
b = False  # boolean
c = 4+5j  # complex

print(x, y, z, a, b, c)
# Solo cuando son str
# print(x+' '+y+' '+z+' '+a+' '+b+' '+c)

# Conocer el tipo de datos de una variable
print(type(b))

# Conversiones de tipos de datos

# Enteros
x = int(2)
print(x)
x = int(2.8)
print(x)
x = int("2")
print(x)

# Float
x = float(2)
print(x)
x = float(2.8)
print(x)
x = float("2")
print(x)
x = float("2.5")
print(x)

# String
x = str(2)
print(x)
x = str(2.8)
print(x)
x = str("2")
print(x)

# Manejo de cadena de textos y algunos metodos

cad = "Hello world"
print(cad[0])
print(cad[0:5])  # No toma el ultimo valor

cad = "   Hello World   "
cad = cad.strip()
print(cad)   # quita espacios al inicio y al final de la cadena

cad = "   Hello World   "
print(len(cad))  # Logitud de cadena
print(cad.lower())  # Cadena en minuscula
print(cad.upper())  # Cadena en mayuscula
print(cad.replace('l', 'y'))  # Remplaza las L por Y
print(cad.split('l'))  # Divide la cadena cadaves que encuente la letra L

# Operaciones
#  se debe importar la libreria import math
# Operciopnes Aritmeticas
a = 2
b = 3
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b  # Cociente
print(c)
c = a // b  # Parte entera de la division
print(c)
c = a % b  # Residuo
print(c)
c = a ** b  # Exponente
print(c)
c = math.sqrt(a)  # Raiz
print(c)


# Captura por consola
print("Digite el nombre")
nombre = input()
print("Holla "+nombre+"!")

# Condiciones

a = 2
b = 1

if a > b:
    print(a, 'Es mayor que', b)
else:
    print(b, "Es mayor que", a)

if b > a:
    if b > 1:
        print(b, "Es mayor que 1 y es mayor que", a)

if a == b:
    print("Son Iguales")
elif a > b:
    print(a, " Es mayor que", b)
else:
    print(b, "Es mayor que", a)

if a == b and a > 2:
    print(a, "Es igual a", b, "Mayor que 2")

if a == b or a > 2:
    print(a, "Es igual a", b, "Mayor que 2")       






