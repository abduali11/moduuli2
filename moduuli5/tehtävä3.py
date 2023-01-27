"Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku "
"Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään"
"Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan."
"Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7"
luku = 0
user = int(input("syötä jokin luku"))

for i in range(1,user):
    if user % i== 0:
        luku = luku +1

    if luku <= 1:
        print("alku luku on" + str(user))
    else:
        print("luku ei ole alku luku" + str(user))


