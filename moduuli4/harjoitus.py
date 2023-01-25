#number = 1
#while number <= 5:
#    print("tulostetaan jotain, kierrosta " + str(number))
#    number = number + 1
#print("suoritus loppui")
#print("number muuttujan arvo lopuksi" + str(number))
#todo mitä ope teki tunnill
#number = 1
#while number <= 5:
#    print("tulostetaan jotain, kierrosta " + str(number))
#    number = number + 1
#print("suoritus loppui")
#print("number muuttujan arvo lopuksi" + str(number))
#jos haluut alkaa 1 numerost tää kaava printin yläpuolelle  number = number + 1

#command = input("anna komento:")
#while command == "jatka":
#    print("jatketaan sitten")
#    command = input("anna komento")
#print("ohjelman suoritus loppuu")


#command = input("anna komento:")
#while command != "lopeta":
#    print("jatketaan sitten")
#    command = input("anna komento")
#print("ohjelman suoritus loppuu")

#application_running = True
#while application_running:
#    command = input("anna komento ")
#    if command == "lopeta":
#     application_running = False
#    else:
#        print("ok, jatketaan sitten")
#        print("jatketaan suoritusta")
#print("ohjelman suoritus loppuu")

#komento = input ("Anna komento: ")
#while komento!="lopeta":
#    print ("Suoritan toiminnon: " + komento)
#    komento = input("Anna komento: ")
#print ("Toiminnot lopetettu.")

#tuuma = float(input("mikä tuuma on senttimetreinä"))
#tuuma = tuuma * 2.54
#print(tuuma)
#if tuuma <0:
#    print("wrong input")
#todo laskee tuuman senttimetreinä ja jos se on alle 0 nii se ei tunnista syötettä
#tuuma = float(input("mikä tuuma on senttimetreinä!! "))
#tuuma = tuuma * 2.54
#while tuuma>0:
#    print("tuuma on senttimetreinä" + str(tuuma))
#    tuuma = float(input("anna tuuma"))
#    print("väärä syöte")

#todo moduuli 4 tehtävä 4
#import random
#random_num = random.randint(0,10)
#print("random numero " + str(random_num))
#guess = int(input("mikä on sun arvaus"))

#while guess != random_num:
#    print("väärä vastaus")
#    if guess <= random_num:
#        print("vastauksesi on liian pieni")
#        guess = int(input("arvaa uudelleen"))
#    if guess >= random_num:
#        print("vastauksesi on liian iso")
#        guess = int(input("arvaa uudelleen"))
#print("oikea arvaus")

#todo moduuli 4 tehtävä 5
#käyttäjänimi = "python"
#salasana = "rules"
#
#käyttäjätunnus = input("anna käyttäjä tunnus")
#salasana_input = input("anna salasana")

#while käyttäjänimi != käyttäjänimi or salasana!=salasana_input:
 #     input("yritä uudelleen")
#print("tervetuloa")

import random

num_of_dice = int(input("Kuinka monta arpakuutiota haluat heittää? "))
dice_sum = 0

for i in range(num_of_dice):
  roll = random.randint(1, 6)
  dice_sum += roll

print("Silmälukujen summa on: ", dice_sum)

