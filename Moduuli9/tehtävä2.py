

"Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan "

"nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. "


"Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa."

"Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. "

"Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. "

"Tulosta tämän jälkeen auton nopeus. "

"Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus"

"Kuljettua matkaa ei tarvitse vielä päivittää."



class Auto:
    def __init__(self, rekkari, huippunopeus, ):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.matka = 0
    def kiihtyvyys(self,muutos):
        uusi_nopeus = self.nykyinen_nopeus + muutos
        if uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        else:
            self.nykyinen_nopeus = uusi_nopeus

        print(f"auton nopeus on {self.nykyinen_nopeus} km/h")

auto = Auto("ABC-123", 142)
print(f"{auto.rekkari} ,  {auto.huippunopeus} ,  {auto.nykyinen_nopeus} , {auto.matka}")

auto.kiihtyvyys(30)
auto.kiihtyvyys(70)
auto.kiihtyvyys(50)



auto.kiihtyvyys(-200)
print(f"auton nopeus hätäjarrutuksen jälkeen on {auto.nykyinen_nopeus} km/h")


