"Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän"
"Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä"
"tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan"
"maksimisilmäluku joka kysytään käyttäjältä ohjelman suorituksen alussa"

import random



maksimi = int(input("kerro luku"))
def heitostatulee(maksimi):
    return random.randint(1, maksimi)

noppa = 0
lukusum = 0

while noppa != maksimi:
    lukusum = 1 + lukusum
    noppa = heitostatulee(maksimi)

print(lukusum)
