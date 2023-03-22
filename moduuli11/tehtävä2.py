"Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. "
"Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena "
"on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan "
"rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun "
"asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton"
"(ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin"
"autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat"


class Auto1:
    def __init__(self, rekkari, huippunopeus):
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

class Sähköauto(Auto1):
    def __init__(self, rekkari, huippunopeus, akkukapaseetti):
        self.akkukapaseetti = akkukapaseetti
        super().__init__(rekkari,huippunopeus)

    def tulosta_tiedot(self):
        print(f"Rekkari: {self.rekkari} Huippunopeus: {self.huippunopeus} Akkukapaseetti: {self.akkukapaseetti} " )


class Moottoriauto(Auto1):
    def __init__(self,rekkari,huippunopeus,bensa):
        super().__init__(rekkari,huippunopeus)
        self.bensa = bensa

    def tulosta_tiedot(self):
        print(f"Rekkari: {self.rekkari} Huippunopeus: {self.huippunopeus} Bensan kulutus: {self.bensa}")

auto1 = Sähköauto("ABC-15", 180 , 52.5)
auto2 = Moottoriauto("ACD-123", 165 , 32.3)

auto1.kiihtyvyys(150)
auto2.kiihtyvyys(150)
auto1.kulje(3)
auto2.kulje(3)

auto1.tulosta_tiedot()
auto2.tulosta_tiedot()