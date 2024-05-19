# Operadores relacionales
"""
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""
resultado = 10 != 20
print (resultado)


# Operadores Lógicos
"""
and y 
or o
--------- PRIORIDADES ----------
not
and
or
"""
a = 10
b = 15
c = 20
res = not((a>b) or (b<c)) # El not lo niega
print(res)
print('-----------------------')
# Operadores de asignación
a = 0
a += 5  # suma en asignación
a -= 2  # resta en asignación
a *= 3  # multiplicación en asignación
a /= 3  # división en asignación
a **= 2 # potencia en asignación
a %= 2  # módulo en asignación

print(a)

print('-----------------------')
# Salida con format
nombre = "Néstor"
edad = 23
print ("Hola {} tienes {} años de edad".format(nombre, edad))
print(f"Hola {nombre} tienes {edad} años de edad")










