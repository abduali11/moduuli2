import math #MUISTA AINA IMPORT MATH

säde = input("ympyrän säde")
säde = float(säde)
pintaala = math.pi * säde * säde
print("ympyränpintala on:" + str(pintaala))


#todo toinen tapa tehdä
r = float(input("anna ympyrän säde:"))
print(f"{r}")
area = math.pi * r * r
print("ympyrän ppinta-ala on:" + str(area))
