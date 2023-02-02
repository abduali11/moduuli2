"Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja."
"Ohjelma palauttaa listassa olevien lukujen summan"
"Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan"

#funtio saa parametrina listan
#ohjelma palauttaa listassa olveine kokonaislukujen summan
def summaa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

             #pääohjelma alkaa
#luodaan lista joka sisältää kokonaislukuja
luvut = [1,2,3,4,5,6,7,8,9]


#pääohjelma kutsuu funktiota, ohjelman täytyy antaa parametreinä jonkun lista funktiolle
#lisäksi pääohjelman täytyy ottaa taltaaan funktion palauttama vastaus

tulos = summaa(luvut)

#tulostetaan funktion palauttama vastaus
print(f"listassa olevien lukjen summa = {tulos}" )