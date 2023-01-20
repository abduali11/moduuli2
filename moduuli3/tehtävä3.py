#"Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l)."
#"Ohjelma ilmoittaa,onko hemoglobiiniarvo alhainen, normaali vai korkea".

#"Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#"Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l."
#todo try ja except

sukupuoli = input("anna sukupuoli ")
hemoglobiiniarvo = float(input("anna hemoglobiiniarvo"))
if sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo > 195:
        print("hemoglobiiniarvo on korkea")
    else:
        print("hemoglobiini arvo on normaali")
if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo > 195:
        print("hemoglobiiniarvo on korkea")
    else:
        print("hemoglobiini arvo on normaali")

