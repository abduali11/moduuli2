""" Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""
#print(f"numerolukon koodi: {code}")
import random

random_number1 = random.randint(0,9)
random_number2 = random.randint(0,9)
random_number3 = random.randint(0,9)
code = str(random_number1) + str(random_number2) + str(random_number3)
print("kolmenumeroinen koodi on " + str(random_number1) + str(random_number2) + str(random_number3))
# toi tapa on helmpompi voi myös tehdä tällä tavalla
#print(f"numerolukon koodi: {code}")

#TODO nelinumeroinen koodi

random_number1 = random.randint(1,6)
random_number2 = random.randint(1,6)
random_number3 = random.randint(1,6)
random_number4 = random.randint(1,6)
code = str(random_number1) + str(random_number2) + str(random_number3) + str(random_number4)
print("nelinumeroinen koodi on " + str(random_number1) + str(random_number2) + str(random_number3) + str(random_number4))

#print(f"numerolukon koodi nelinumeroinen: {code}")