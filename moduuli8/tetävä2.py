"Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä"
"maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on"
"saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne"

import mysql.connector
"maakoodi on country code"

def country_name(country_code):
    sql =f" SELECT type, count(type), FROM airpot, WHERE iso_country= fi"'group by type'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='abdu1',
         password='abdu1',
         autocommit=True
         )

country_code = input("syötä on country_code:")
tulos = country_name(country_code)

for i in tulos:
    print(tulos)