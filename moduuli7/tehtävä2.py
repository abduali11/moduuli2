"Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka"
"kunnes käyttäjä syöttää tyhjän merkkijonon"
"Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan"
"syötettiinkö nimi ensimmäistä kertaa"
"Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä"
"Käytä joukkotietorakennetta nimien tallentamiseen"

# luodaan tyhjä joukko (käytettävä set-toimintoa)
nimet = set()

nimi = input("anna nimi")


# toistetaan, kunnes saadaan tyhjä merkkijono
while nimi !="":
    if nimi in nimet:
        nimi = input("anna nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)
    nimi = input("anna nimi")

for i in(nimet):
    print(i)

