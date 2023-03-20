"Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan."
"Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä."
"Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena."
"Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen."
"Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."

class Hissi:
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, uusi_kerros):
        while uusi_kerros > self.kerros:
            self.kerros_ylös()
        while uusi_kerros < self.kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(ylin_kerros, alin_kerros) for i in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        hissi = self.hissit[hissi_numero - 1]
        print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}")
        hissi.siirry_kerrokseen(kohde_kerros)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(3, 3)



