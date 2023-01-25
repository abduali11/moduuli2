"Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta"
"siihen asti, ""kunnes tämä arvaa oikein."
"Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein." \


" Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä."

import random
random_num = random.randint(0,10)
print("random numero " + str(random_num))
guess = int(input("mikä on sun arvaus"))

while guess != random_num:
    print("väärä vastaus")
    if guess <= random_num:
        print("vastauksesi on liian pieni")
        guess = int(input("arvaa uudelleen"))
    if guess >= random_num:
        print("vastauksesi on liian iso")
        guess = int(input("arvaa uudelleen"))
print(f"arvasit oikein")

