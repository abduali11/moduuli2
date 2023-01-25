"Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat"
"väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein" \
" tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä " \
"Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules)."

käyttäjänimi = "python"
salasana = "rules"
yrityksiä = 0
käyttäjätunnus = input("anna käyttäjä tunnus")
salasana_input = input("anna salasana")

while yrityksiä<=5:
    print(yrityksiä)
    if käyttäjätunnus != käyttäjänimi or salasana!=salasana_input:
        käyttäjätunnus = input("anna käyttäjä tunnus")
        salasana_input = input("anna salasana")
        yrityksiä = yrityksiä + 1
    elif käyttäjänimi == "python" and salasana == "rules":
        print(input("tervetuloa"))
if käyttäjätunnus != käyttäjänimi or salasana!=salasana_input:
    print("pääsy estetty")
