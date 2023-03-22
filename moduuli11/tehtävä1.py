"Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. "

"Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja."
"Kirjoita luokkiin myös tarvittavat alustajat."

"Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. "
"Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua)."

"Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla."

class Julkaisu:
    def __int__(self, nimi):
        self.nimi = nimi
class Kirja(Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__int__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.kirjoittaja} {self.sivumäärä} {self.nimi}")

class Lehti(Julkaisu):
    def __init__(self, toimittaja,nimi):
        self.toimittaja = toimittaja
        super().__int__(nimi)

    def tulosta_tiedot(self):
        print(f"{self.nimi} {self.toimittaja}" )

akkari = Lehti("Aku Ankka","Aki Hyyppä")
hytti = Kirja("N:0 6", "Rose Liksom", "200 sivua")

akkari.tulosta_tiedot()
hytti.tulosta_tiedot()
