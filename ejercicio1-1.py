#Ejercicio 1.1. Escribir un programa que pregunte al usuario:
#a)su nombre, y luego lo salude.
#b)dos números, y luego muestre el producto

nombre = str(input("Escribe tu nombre: "))
print("Hola {0}".format(nombre))

numero1 = int(input("Ingresa el primer  número: "))
numero2 = int(input("Ingresa el segundo número: "))

print("El producto de los números ingresador es: {0}.".format(numero1 * numero2))

