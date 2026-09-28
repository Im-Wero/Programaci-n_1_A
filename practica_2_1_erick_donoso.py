#Ejercicio: Datos presonales
nombre = "Erick"
edad = 20
ciudad = "Guadalajara"
print ("Hola, yo soy", nombre, "tengo", edad, "y soy de", ciudad)

#Actualizar un contador
contador = 0
contador = contador + 1
print ("Contador:", contador)
contador = contador + 1
print ("Contador:", contador)
contador = contador + 1
print ("Contador:", contador)

#Ejercicio: Constante de conversión
PULGADAS_A_CENTIMETROS = 2.54
pulgadas = 10
print (pulgadas, "pulgadas son", pulgadas * PULGADAS_A_CENTIMETROS, "centímetros")

#Ejercicio: Area de un triángulo
base = 5
altura = 10
area = (base * altura) / 2
print ("El área del triángulo es:", area)

#Ejercicio: Total con IVA
IVA = 0.19
precio = 800
total = precio + (precio * IVA)
print ("El total con IVA es:", total)
precio = 1500
total = precio + (precio * IVA)
print ("El total con IVA es:", total)

#Ejercicio: Intercabio de valores
temp = 0
a = 7
b = 6
print ("Valores iniciales: a =", a, "b =", b)
c = a
a = b
b = c
print ("Valores intercambiados: a =", a, "b =", b)

#Identificar tipos con la función type()
alumnos = 30
radio = 3.14
nombre = "Erick"
es_mayor_de_edad = True
print ("El tipo de dato de numero entero es:", type(alumnos))
print ("El tipo de dato de radio es:", type(radio))
print ("El tipo de dato de nombre es:", type(nombre))
print ("El tipo de dato de es_mayor_de_edad es:", type(es_mayor_de_edad))

#Ejercicio: Convertir tipos
texto = 4
print ("El tipo de dato de numero es:", type(texto),texto)
numero = str(texto)
print ("El tipo de dato de numero es:", type(numero),numero)

#Ejercicio: Booleanos y comparaciones
a = 5
b = 10
c = a < b
print ("El tipo de dato de c es:", type(c))
print ("El valor de c es:", c)