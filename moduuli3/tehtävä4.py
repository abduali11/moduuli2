#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi""
"Vuosi on karkausvuosi, jos se on jaollinen neljällä"
"Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla."

vuosiluku = int(input("anna vuosiluku"))
if vuosiluku % 4 == 0 and vuosiluku % 100 != 0:
    print("karkausvuosi on " + str(vuosiluku))
elif vuosiluku % 400 == 0:
    print("karkausvuosi on " + str(vuosiluku))
else:
    print("ei ole karkausvuosi")
