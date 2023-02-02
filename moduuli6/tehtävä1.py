"Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6."
"Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen"
"Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun"

import random
tulos = 0
def heitostatulee():
    return random.randint(1 , 6)


while tulos !=6:
    tulos = heitostatulee()
    
    print(tulos)




