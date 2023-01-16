
leiviskat = float(input("Kuinka monta leiviskää? "))
naulat = float(input("Kuinka monta naulaa? "))
luodit = float(input("Kuinka monta luotia? "))
#leiviskan sain 20*32*13.3/100000
#naulan sain 13.3/1000
#luodit sain 13.3/1000
massa_kg = (leiviskat * 0.016) + (naulat * 0.0013) + (luodit * 0.0041)
massa_g = massa_kg * 1000

print("Massa on " + str(massa_kg) + " kilogrammaa tai " + str(massa_g) + " grammaa.")


