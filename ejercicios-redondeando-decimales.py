# Ejercicio 04
import math
radio = float(input("Ingrese el radio: "))
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio
print (f"El area de la circ. es: {area:.3f}")
print (f"La longitud de la circ. es: {longitud:.3f}")

#      :.3f son para decimales


# Ejercicio 05
precio_total = float(input("Ingrese el precio: "))
descuento = precio_total * 0.15
precio_final = precio_total - descuento
print(f"Precio sin desc. es: {precio_total:.2f}")
print(f"Descuento es: {descuento:.2f}, equivale a 15%")
print(f"Precio final es: {precio_final:.2f}")