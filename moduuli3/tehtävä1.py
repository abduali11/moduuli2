
#rahat = float(input("anna rahamäärä"))
#if rahat>=5:
#    print("voit ostaa latten")


#ika = int(input("anna ikäsi"))
#if ika >= 18:
#     print("olet siis täysi-ikäinen")
#     aika = ika - 18
#     print("olet ollut sitä" + str(aika) + "vuotta")

#mun oma keksimä koodi mikä toimii
#kakku = int(input("kakku maksaa"))
#if kakku>=18:
#    raha = kakku - 18
#    print("kiitos ostoksestasi" + str(raha) + " ja hyvää päivän jatkoa"

"Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.""Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin"
"järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu"
"Kuha on alamittainen, jos sen pituus on alle 37 cm."

kuha = float(input("kuhan pituus"))
if kuha<=37:
    puuttuu = kuha - 37
    print("kuhasta puuttuu cm " + str(kuha - 37))

