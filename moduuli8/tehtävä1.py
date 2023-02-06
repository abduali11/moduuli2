
import mysql.connector

"Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin"
"Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen"
"sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta"
"ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen"

def get_name(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
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

icao = input("syötä on ICAO-koodi:")
tulos = get_name(icao)

for i in tulos:
    print(f"{i[0]} sijaintikunta on {i[1]}")










