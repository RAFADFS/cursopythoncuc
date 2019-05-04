# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:07:45 2019

@author: android
"""
print("Digite su edad")
edad = input()
edad = int(edad)
"""
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor edad")
    """
# Si Sino de linea
print('Es mayor de eda') if edad >= 18 else print('Menor de edad')

# SI de linea
if edad >= 18: print("Es Mayor de edad")

# Arrays
v = ["hola", "Mundo", 4, 3.4, True, ["otra", "array", "dentro"]]
v1 = [1, 2, 3, 4]
v2 = range(201)
v3 = range(1, 201)
v4 = ["dentro",  "esta"]
# recorrer un vector
for x in v3:
    print(x)
# Acceder al elemento
print(v[2])

# Modificar el elemento
v1[2] = "Rafa"

# Eliminar elemento
v4.remove("dentro")

# Elimina el ultimo elemento o posicion
v.pop()  # elimina la ultima posicion
v.pop(4)  # elimina el elemento en la posicion 4

# Agregar elemento
v.append(5)  # agraga el elemento 5 a la ultima posicion
v.insert(3, "fajardo")  # agrega en la posicion 3 el elemento fajardo

# Borrar elementos
# v3.clear
# Conocer la posicion de un elemento
v.index("hola")

# Cantidad de elementos
len(v)

# Cuantas veces aparece un elemento en el vector
v.append("otra")
v.count("otra")

# Ordenar un vector
a = [5, 8, 2, 4, 6, 7, 3, 1]
a.sort()

a = 6 in a  # verificar si el elemneto 6 esta en el vector a
print(a)

# Aceder a un elemento arrays dentro de otro arrays
v5 = ["hola", "Mundo", 4, 3.4, True, ["otra", "array", "dentro"]]

# forma 1
aux = v5[-1]
aux = aux[0]
print(aux)

# forma 2
aux = v5[-1][0]
print(aux)

# Recorrer Vector
for x in v5[:5]:
    print(x)
# recorrer un vector saltando posiciones
b = [5, 8, 2, 4, 6, 7, 3, 1]
for x in b[0::2]:  # recorre el ventor completo de 2 en 2
    print(x)

# sumar los numeros hasta n
# forma 1
print("Digite tope")
cant = input()
cant = int(cant)
suma = 0
for x in range(cant+1):
    suma = x+suma
print(" la suma es : ", suma)

# forma 2
print("Digite tope")
cant = int(input())
sumatoria = sum(range(cant+1))
print("la sumatoria es: ", sumatoria)


# while
i = 1
while i < 5:
    print(i)
    i = i + 1


# Procedimeinto no retorna valor
def hola_mundo():
    print("hola mundo")


# Invocar el Procedimiento
hola_mundo()


# Funciones que retorna valor
def elevar_cuadrado(numero):
    return numero ** 2


# Invocar la funcion
elevar_cuadrado(3)





