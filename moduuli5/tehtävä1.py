"Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän"
"Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan"
"Käytä for-toistorakennetta."
import random

nopan_summa = 0
noppa = int(input("monta noppaa haluat heittää"))
for i in range(noppa):
    arpakuutio = random.randint(1,6)
    print(arpakuutio)
    nopan_summa = noppa + nopan_summa
print("silmä lukujen summa on " + str(nopan_summa))
