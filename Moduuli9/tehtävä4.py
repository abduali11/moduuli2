"Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi."


"Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta."

"Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä."


"Rekisteritunnus luodaan seuraavasti ABC-1, ABC-2 jne. Sitten kilpailu alkaa"


"Jokaisen auton nopeutta muutetaan siten, että ###nopeuden ##muutos arvotaan väliltä -10 ja +15 km/h väliltä."


"Tämä tehdään kutsumalla kiihdytä-metodia."

"Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia."

"Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä."

"Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."

import random

class Auto1:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.matka = 0

    def kiihtyvyys(self, muutos):
        uusi_nopeus = self.nykyinen_nopeus + muutos
        if uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.matka += self.nykyinen_nopeus * tuntimaara

    def tulosta_ominaisuudet(self):
        print("-----------------------------------------------------------")
        print(f"/Rekisteritunnus/: {self.rekkari}, /huippunopeus/: {self.huippunopeus}, /matka/: {self.matka} km")


A_lista = []
for i in range(1 , 11):
    autot = Auto1(f"ABC-{i}", random.randint(100, 200))
    A_lista.append(autot)

while True:
    for auto in A_lista:
        muutos = random.randint(-10, 15)
        auto.kiihtyvyys(muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            break
    else:
        continue
    break

for auto in A_lista:
    auto.tulosta_ominaisuudet()









