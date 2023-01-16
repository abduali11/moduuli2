#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
# kokonsluku on int
import math

num1 = int(input("anna ensimmäinen luku"))
num2 = int(input("anna toinen luku"))
num3 = int(input("anna kolmas luku"))
sum = num1 + num2 + num3
tulo = num1 * num2 * num3
keskiarvo = ((num1 + num2 + num3)) / 3
print("lukujen tulo on " + str(tulo))
print("lukujen summa on " + str(sum))
print("lukujen keskiarvo on " + str(((num1 + num2 + num3)) / 3))