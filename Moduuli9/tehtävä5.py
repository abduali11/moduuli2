"Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi."
"Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta."
"Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä."
"Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne."
"Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:"

"Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä."
"Tämä tehdään kutsumalla kiihdytä-metodia".
"Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia."
"Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä"
"Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna"




"Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan "

"nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. "


"Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa."

"Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. "

"Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. "

"Tulosta tämän jälkeen auton nopeus. "

"Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus"

"Kuljettua matkaa ei tarvitse vielä päivittää."


def kiihtyvyys(self, muutos):
    uusi_nopeus = self.nykyinen_nopeus + muutos
    if self.nykyinen_nopeus > self.huippunopeus:
        muutos < 0
    elif