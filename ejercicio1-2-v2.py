#Ejercicio 1.2. Implementar algoritmos que permitan:
#	a) Calcular el perímetro de un rectángulo dada su base y su altura.
#	b) Calcular el área de un rectángulo dada su base y su altura.
#	c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas
#	x1, x2, y1, y2.
#	d) Calcular el perímetro de un círculo dado su radio.
#	e) Calcular el área de un círculo dado su radio.
#	f) Calcular el volumen de una esfera dado su radio.
#	g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

#Resolución punto a)
def calcularPerimetroRectangulo():
	base   = int(input("Ingrese la base del rectangulo: "))
	altura = int(input("Ingrese la altura del rectangulo: "))
	resultado = 2 * (base + altura)
	print("El perimetro del rectangulo es: {0}".format(resultado))

#Resolución punto b)
def calcularAreaRectangulo():
	base   = int(input("Ingrese la base del rectangulo: "))
	altura = int(input("Ingrese la altura del rectangulo: "))
	resultado = base * altura
	print("El area del rectangulo es: {0}".format(resultado))

#Resolución punto c)
def calcularAreaCoordenadasRectangulo():
	x1 = int(input("Ingrese la primer coordenada de X: "))
	x2 = int(input("Ingrese la segunda coordenada de X: "))
	y1 = int(input("Ingrese la primer coordenada de Y: "))
	y2 = int(input("Ingrese la segunda coordenada de Y: "))
	base = x2 - x1
	altura = y2 - y1
	resultado = base * altura
	print("El area del rectangulo es: {0}".format(resultado))

#Resolución punto d)
def calcularPerimetroCirculo():
	radio = float(input("Ingresar el radio del circulo: "))
	resultado = float(2*3.14*radio)
	print("El perimetro del circulo es: {0:0.02f}.".format(resultado))

#Resolución punto e)
def calcularAreaCirculo():
	radio = float(input("Ingresar el radio del circulo: "))
	resultado = float(3.14*radio**2)
	print("El area del circulo es: {0:0.02f}.".format(resultado))

#Resolución punto f)
def calcularAreaEsfera():
	radio = float(input("Ingresar el radio de la esfera: "))
	resultado = float((4/3)*3.14*radio**3)
	print("El area de la esfera es: {0:0.02f}.".format(resultado))

#Resolución punto g)
def calcularHipotenusa():
	a = int(input("Ingrese el valor del cateto horizontal: "))
	b = int(input("Ingrese el valor del cateto vertical: "))
	resultado = math.sqrt(a**2 + b**2)
	print("La hipotenusa es: {0:0.02f}.".format(resultado))
	
continua = True
while(continua):
	print("""Elija una opción:
	            1. Calcular el perimetro de un rectangulo
	            2. Calcular el area de un rectangulo
	            3. Calcular el area de un rectangulo según sus coordenadas
	            4. Calcular el perimetro de un circulo
	            5. Calcular el area de un circulo
	            6. Calcular el area de una esfera
	            7. Calcular la hipotenusa, según sus catetos
	            8. Salir""")
	print("\n"*2)
	try:	
		entrada = int(input("ingrese una opción: "))
		if (type(entrada) == int):
			if entrada  == 1:
				calcularPerimetroRectangulo()
			elif entrada == 2:
				calcularAreaRectangulo()
			elif entrada == 3:
				calcularAreaCoordenadasRectangulo()
			elif entrada == 4:
				calcularPerimetroCirculo()
			elif entrada == 5:
				calcularAreaCirculo()
			elif entrada == 6:
				calcularAreaEsfera()
			elif entrada == 7:
				calcularHipotenusa()
			elif entrada == 8:
				continua = False
				print("Ha decidido Salir!...")
			else:
				print("Ha presionado una tecla o un valor no reconocido.")
				
	except:
		print("No se permiten este tipo de ingresos.")
	print("Presione una tecla para continuar")
	input()
