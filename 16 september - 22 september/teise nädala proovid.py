# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#print("Sisesta PIN-kood:")
#sisestatud_pin = input()
#if sisestatud_pin == "1234":
#    print("Sisenesid pangaautomaati!")
#else:
#    print("Vale parool! Enesehävitusrežiim aktiveeritud: 3 ... 2 ... 1 ....")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#vastus = "0" + "0" + "7"
#if vastus == "007":
#    print("On võrdsed!")
#else:
#    print("Ei ole võrdsed!")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#print("Kui vana oled?")
#vanus = int(input())
#
#if vanus < 14:
#    print("Oled natukene noor edasipääsuks.")
#else:
#    print("Sisenesid võlumaailma.")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#vastus = 2 + 2 * 3
#if vastus == 12:
#    print("On võrdsed!")
#else:
#    print("Ei ole võrdsed!")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#kontoseis = 100
#
#print("Sisesta PIN-kood:")
#sisestatud_pin = input()
#if sisestatud_pin == "1234":
#    print("Sisenesid pangaautomaati! Pangakontol on " + str(kontoseis) + " eurot.")
#    print("Sisesta, mitu eurot soovid välja võtta:")
#    soovitud_raha = int(input())
#    if soovitud_raha <= kontoseis:
#        kontoseis = kontoseis - soovitud_raha  # kontoseisu väärtus väheneb
#        print("Raha välja võetud: " + str(soovitud_raha) + " eurot.")
#    else:
#        print("Kontol ei ole nii palju raha!")
#    print("Pangakontol on järgi: " + str(kontoseis) + " eurot.")
#else:
#    print("Vale parool! Enesehävitusrežiim aktiveeritud: 3 ... 2 ... 1 ....")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#a = 1
#b = 2
#if a > b:
#    if a == 1:
#        print(a)
#    else:
#        print(b)
#else:
#  print("Olen siin")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#from random import randint
#
#suvaline_arv = randint(1, 2)
#if suvaline_arv == 1:
#    arvuti_valik = "kull"
#else:
#    arvuti_valik = "kiri"
#
#print("Mündiviskes võitis: " + arvuti_valik)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#from random import randint
#
#print("Kas kull (1) või kiri (2)?")
#kasutaja_valik = int(input())
#suvaline_arv = randint(1, 2)
#
#if kasutaja_valik == suvaline_arv:
#    print("Arvasid õigesti.")
#else:
#    print("Arvasid valesti.")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIIIValikulause1
#arv = 6
#if arv > 6:
#    print("Arv on liiga suur!")
#elif arv < 6:
#    print("Arv on liiga väike!")
#else:
#    print("Õige arv!")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVSoned
#print("Jim ütles vaid: "Siin see on."")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVSoned
#print("Minu lemmikraamatud on \n\"Kevade\" ja \n\"Rehepapp\"")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVSoned
#print("""Rock 'n' rolli Jim ütles vaid: "Siin see on." """)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVSoned
#nimi1 = "Otto"
#nimi2 = "Triin"
#print("Tere,",nimi1)
#print(nimi2 + "!")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVSoned
#print("tartu".capitalize())
#print("Tartu".endswith("tu"))
#print("Tartu".lower())
#print("Tartu".upper())
#print("Tartu".startswith("tu"))
#print("Kauneim linn on Eestis Tartu".title())

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVKilpkonn
#from turtle import *
#
#color("red")  # Kilpkonn muutub punaseks
#begin_fill()  # Kilpkonn alustab ringi värvimist
#circle(100)  # Kilpkonn joonistab ringi raadiusega 100 pikslit
#end_fill()  # Kilpkonn lõpetab ringi värvimise
#
#exitonclick()

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTIVKilpkonn
from turtle import *
from random import randint

värv = randint(1, 3)
if värv == 1:
    color("blue")  # Sinine
if värv == 2:
    color("black")  # Must
if värv == 3:
    color("white")  # Valge valgel taustal
begin_fill()  # Kilpkonn alustab ringi värvimist
circle(100)  # Kilpkonn joonistab ringi raadiusega 100 pikslit
end_fill()  # Kilpkonn lõpetab ringi värvimise

exitonclick()