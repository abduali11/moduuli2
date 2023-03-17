"Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän"


"Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt"


"Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h."

"Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km."

class Auto:
    def __init__(self, rekkari, huippunopeus,):
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


    def kulje(self, tuntimaara):
        self.matka += self.nykyinen_nopeus * tuntimaara


auto = Auto("ABC-123",142)



auto.kiihtyvyys(30)
auto.kiihtyvyys(70)
auto.kiihtyvyys(50)



print(f"Kuljettu matka {auto.matka} km")

print(f"{auto.rekkari} ,  {auto.huippunopeus} ,  {0} ,")


print(f"auton nopeus on {auto.nykyinen_nopeus} km/h")

auto.kulje(1.5)
auto.kiihtyvyys(-200)
print(f"auton nopeus hätäjarrutuksen jälkeen on {auto.nykyinen_nopeus} km/h")
print(f"kuljettu matka on {auto.matka} metriä")

