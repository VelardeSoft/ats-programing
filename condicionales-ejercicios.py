# Condicionales

numero = int(input("Numero: "))
if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero < 0:
    print(f"El numero {numero} es negativo")
else:
    print(f"El numero es CERO")


# Condicionales combinadas
edad = int(input("Edad: "))
if 0 <= edad <= 120:
    print ("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print ("Edad incorrecta")



# Ejercicio 1 de condiciones
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
p1 = num1 % 2 == 0
p2 = num2 % 2 == 0
if p1 and p2:
    print(f"Ambos numeros {num1} y {num2} son PARES")
elif p1 == True:
    print(f"El numero {num1} es PAR")
elif p2 == True:
    print(f"El numero {num2} es PAR")
else:
    print(f"Los numeros {num1} y {num2} son IMPARES")



# Ejercicio 2 de condiciones
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n1 > n2 and n1 > n3:
    print(f"El numero {n1} es el mayor")
