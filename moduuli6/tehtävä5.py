def summaa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa


def summaa2(lista2):
    summa2 = 0
    for luku2 in lista2:
        if luku2 % 2 == 1:
            summa2 += luku2
    return summa2

luvut = [1,2,3,4,5,6,7,8,9]
parittomat = [1,2,3,4,5,6,7,8,9]

tulos = summaa(luvut)
tulos2 = summaa2(parittomat)
print("lukujen summa " + str(tulos))
print("lukujen summa" + str(tulos2))