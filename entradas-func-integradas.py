# Entrada de datos

nombre = input("Digite su nombre: ") # Tipo cadena
print(f"Hola {nombre}!")
numero = int(input("Ingrese un numero: ")) # Tipo entero
print (f"El numero es: {numero}")


# Funciones Integradas

n = int("10") # Convertir a entero
f = float("10.5") # Convertir a flotante
txt = str(10) # Convertir a cadena
binary = bin(10) # Convertir a binario
hexa = hex(10) # Convertir a hexadecimal
octal = oct(10) # Convertir a octal
redondea = round(5.5) # Redondear
print (redondea)
cantidad = len("Velarde") # Longitud de la cadena


# Ejercicio 01
a = float(input("Ingrese A: "))
b = float(input("Ingrese B: "))
c = float(input("Ingrese C: "))

resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print (f"El resultado es: {resultado}")



# Ejercicio 02
resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a < b)

print ("------- EJERCICIO 02 -------")
print (resultado)



# Ejercicio 03
a = 10
b = 5
print (f"A -> {a} \n B -> {b}")

aux = a
a = b
b = aux
print (f"A -> {a} \n B -> {b}")

print ("----------------------------")
a = input("Ingrese A: ")
b = input("Ingrese B: ")
a, b = b, a
print (f"Nuevo valor de A es: {a}")
print (f"Nuevo valor de B es: {b}")