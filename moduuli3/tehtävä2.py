#tämä on esimerkki
#ikä = int(input("Anna ikäsi: "))
#if ikä>=65:
    #print("Olet eläkeiässä.")
#elif ikä>=18:
    #print("Olet työiässä.")
#elif ikä>=7:
    #print("Olet koululainen.")
#else:
    #print("Olet pikkulapsi.")

#"Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa"
#"sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
#"sen sanallisen kuvauksen alla olevan luettelon mukaisesti."
#"LUX on parvekkeellinen hytti yläkannella.
#"A on ikkunallinen hytti autokannen yläpuolella.
#"B on ikkunaton hytti autokannen yläpuolella.
#"C on ikkunaton hytti autokannen alapuolella.

hyttiluokka = input("laivan hyttiluokka ")
if hyttiluokka == "A":
    print("A on ikkunallisen hytin autokannen yläpuolella ")
elif hyttiluokka == "B":
    print("B on ikkunattoman hytin autokannen yläpuolella ")
elif hyttiluokka == "C":
    print("C on ikkunattoman hytin autokkannen yläpuolella ")
elif hyttiluokka == "LUX":
    print("On parvekkeellisen hytin yläpuolella ")
else:
    print("virhe")

