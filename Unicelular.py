"""Versión utilizada 3.7.0

	Integrantes:
	- Aco Guerrero Iván Rogelio
	- Ricardo Hernández Gómez
	- Hernández Arrieta Carlos Alberto
	- Hernández García Luis Angel

Esta formula se obtuvo de la tabla del automata celular
	Tambien se encuentra como la regla 126 de Wolfram
"""

from random import randint
def calculo(arreglo):
	"""
	Calcula los elementos de la siguiente linea
	Por ejemplo si iniciamos con un uno en medio del arregglo, se concateanan 

	Args:
		arreglo: String
	Returns:
		Regresa un cero o un uno
	"""
	a = int(arreglo[0])
	b = int(arreglo[1])
	c = int(arreglo[2])
	return str((a + b + (a * b) + c + (a * c) + (b * c)) % 2)

def imprimeLinea(arreglo):
	"""
	Imprime la linea correspondiente de la figura

	Args:
		arreglo: String
	"""
	espacios = " " * (75 - int(len(arreglo)/2)) # Espacios necesarios antes de imprimir la linea
	# Se reemplazan los "1" con "*" y los "0" con espacios
	arreglo = arreglo.replace("0"," ").replace("1","*")
	print(espacios + arreglo)

def sierpinski(arreglo):
	"""
	Args:
		arreglo: String
	"""
	aux = ""
	# Los ceros son necesarios para realizar el buen calculo inicial y final
	arreglo = "00" + arreglo + "00"
	# En este for se envian bloques de 3 del arreglo
	for x in range(0, len(arreglo) - 2):
		aux += calculo(arreglo[x:x+3])
	# Se hace un limite para que las lineas solo sean de maximo 143 caracteres de largo
	# (Solo es necesario para presentacion)
	if len(aux) >= 143:
		return aux[1:len(aux)-1]
	else:
		return aux

def main():
	"""Función principal main

	Esta Función tiene dos opciones:
	La Primera es iniciar con un arreglo con un elemento inicial en medio o iniciar con elementos aleatorios
	La segunda es que altura quieres que tenga a figura a imprimir
	"""
	print("**** Triangulo de Sierpinski ****")
	print("Escoja una opcion:\n1. Iniciar con un solo elemento\n2. Iniciar con un numero aleatorio")
	opcion = input("Opcion: ")
	print("\nEscoja la altura")
	altura = input("Altura: ")

	if opcion == "1":
		arreglo = "1"
	else:
		arreglo = str(bin(randint(2, 18446744073709551616)))[2:]

	for i in range(0,int(altura)):
		imprimeLinea(arreglo)
		arreglo = sierpinski(arreglo)

#main()
