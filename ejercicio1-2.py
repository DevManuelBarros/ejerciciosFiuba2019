#Ejercicio 1.2. Implementar algoritmos que permitan:
#	a) Calcular el perímetro de un rectángulo dada su base y su altura.
#	b) Calcular el área de un rectángulo dada su base y su altura.
#	c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas
#	x1, x2, y1, y2.
#	d) Calcular el perímetro de un círculo dado su radio.
#	e) Calcular el área de un círculo dado su radio.
#	f) Calcular el volumen de una esfera dado su radio.
#	g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#Resolución punto a)
def calcularPerimetro():
	base   = int(input("Ingrese la base del rectangulo: "))
	altura = int(input("Ingrese la altura del rectangulo: "))
	resultado = 2 * (base + altura)
	print("El perimetro del rectangulo es: {0}".format(resultado))

#Resolución punto b)
def calcularArea():
	base   = int(input("Ingrese la base del rectangulo: "))
	altura = int(input("Ingrese la altura del rectangulo: "))
	resultado = base * altura
	print("El area del rectangulo es: {0}".format(resultado))

#Resolución punto c)
def calcularAreaCoordenadas():
	x1 = int(input("Ingrese la primer coordenada de X: "))
	x2 = int(input("Ingrese la segunda coordenada de X: "))
	y1 = int(input("Ingrese la primer coordenada de Y: "))
	y2 = int(input("Ingrese la segunda coordenada de Y: "))
	base = x2 - x1
	altura = y2 - y1
	resultado = base * altura
	print("El area del rectangulo es: {0}".format(resultado))

	
	

#calcularPerimetro()
calcularArea()
#calcularAreaCoordenadas()
