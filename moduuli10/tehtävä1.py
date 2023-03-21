"Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron."

"Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. "

"Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),"

"Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, "

"missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen "
"siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen."
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            print(f"Virhe kerros {kohde_kerros} on pienempi kuin hissin alin kerros {self.alin_kerros}")
        elif kohde_kerros > self.ylin_kerros:
            print(f"Virhe kerros {kohde_kerros} on suurempi kuin hissin ylin kerros {self.ylin_kerros}")
        else:
            while kohde_kerros > self.nykyinen_kerros:
                self.kerros_ylös()
            while kohde_kerros < self.nykyinen_kerros:
                self.kerros_alas()

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

h = Hissi(alin_kerros=1, ylin_kerros=10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)







