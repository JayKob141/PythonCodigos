from math import pi
print("Calculando el volumen de un cono")

radio = float( input("Introduce el radio de la base: ") )
altura = float( input("Introduce la altura del cono: ") )

volumen = ( pi * (radio*radio) * altura ) / 3
print("El volumen del cono es:", volumen)
