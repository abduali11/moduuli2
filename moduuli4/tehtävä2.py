"Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi"
"niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän"
"Sen jälkeen ohjelma lopettaa toimintansa."
"1 tuuma = 2.54 cm"

tuuma = float(input("mikä tuuma on senttimetreinä!! "))
tuuma = tuuma * 2.54
print(tuuma)
while tuuma>0:
    tuuma = float(input("anna tuuma"))
    print(tuuma * 2.54)
print("ohjelma loppuu")

