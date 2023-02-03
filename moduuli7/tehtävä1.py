








vuodenajat = (" kevät", "kesä", "syksy" , "talvi")

kknumero = int(input("anna on kuukauden numero" ))


if(kknumero == 1 or kknumero == 2 or kknumero == 3 or kknumero == 11 or kknumero == 12):
    vuodenaika = vuodenajat [3]
elif(kknumero == 4 or kknumero == 5):
    vuodenaika = vuodenajat[0]
elif(kknumero == 6 or kknumero == 7):
    vuodenaika = vuodenajat [1]
elif (kknumero == 8 or kknumero == 9 or kknumero == 10):
    vuodenaika = vuodenajat [2]
    print(f"{kknumero} kk on {vuodenaika}")
else:
    print("vuoden aika on tuntematon")

