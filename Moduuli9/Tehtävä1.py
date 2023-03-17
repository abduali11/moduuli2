"Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja"
"kuljettu matka." \
" Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina"
"saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi."

"Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h)."
"Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet."

#class auto:
#    pass
#auto = auto()
#auton_rekkari = "ABC-123"
#auton_huippunopeus = "142 km/h"
#auton_hetki_nopeus = "0 km/h"
#auton_matka = "0 Metriä"

#print(f"{auton_rekkari}, {auton_huippunopeus} ,{auton_hetki_nopeus} ,{auton_matka}")

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", "142 km/h")

print(f"auton rekkari on {auto.rekkari} ,  huppunopeus on {auto.huippunopeus} ,  nopeus {auto.nykyinen_nopeus} ja matka on {auto.matka} km/h")

