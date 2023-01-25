"Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka"
"kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. "
"Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman."



lukuStr = input("anna luku")
big = int(lukuStr)
small = int(lukuStr)

while lukuStr != "":
    luku = int(lukuStr)
    if luku > big:
        big = luku
    elif luku < small:
        small = luku
    lukuStr = input("anna luku")

print("suurin luku on " + str(big))
print("pienin luku on " + str(small))
