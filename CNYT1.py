#Hola, Bienvenido!
#Primero que todo vamos a importar la libreria de python math, esta nos ayudará para hacer algunas operaciones matemáticas.

import math 

#Definimos la suma  
def suma(a,b):
    real = a[0] + b[0]
    imaginario = a[1] + b[1]
    return (real, imaginario)


#Definimos la resta
def resta(c,d):
    real = c[0] - d[0]
    imaginario = c[1] - d[1]
    return (real, imaginario)


#Definimos la multiplicación 

def multiplicacion(a,b):
    real = (a[0] * b[0])-(a[1] * b[1])
    imaginario = (a[1] * b[0])+(a[0] * b[1])
    return (real, imaginario)


#Definimos la división
def division(a,b):
    real = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    imaginario = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    return (real, imaginario)

#Definimos el modulo de un vector.
def modulo(a,b):
    real = (a * a + b * b)**0.5
    return (real)

#Definimos el conjugado
def conjugado(a,b):
    real = a
    imaginario = -b
    return (real, imaginario)


#Definimos las coordenadas polares haciendo uso de la función arcotangente.
def polar(a,b):
    real = (a * a + b * b)**0.5
    imaginario = math.atan(b/a)
    return (real, imaginario)



print("Bienvenido a su libreria de computación cuántica")
print("Realizado por Thomas Feris Riaño")