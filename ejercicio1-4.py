#Ejercicio 1.4. Implementar un algoritmo que, dado un número entero n, permita calcular su
#factorial.

try:
	numero = int(input("Ingrese un número entero: "))
	resultado = 1
	for i in range(2, numero+1):
		resultado *= i
	print(resultado)
except:
	print("Valor invalido") 
