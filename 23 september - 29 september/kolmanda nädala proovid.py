# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel1
#i = 0
#while i < 5:
#    print("Tere!")
#    i = i + 1
#    print(i)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel1
#i = 0
#while i < 5:
#    i = i + 1
#print(i)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel1
#i = 0
#while i <= 5:
#    i = i + 1
#print(i)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel1
#i = 0
#while i == 5:
#    i = i + 1
#print(i)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel1
#from turtle import *
#
#i = 0  # Muutuja i väärtus on esialgu 0
#while i < 4:  # Kilpkonn joonistab tsükli abil ruudu. Tsükli keha läbitakse neli korda.
#    forward(100)
#    left(90)
#    i = i + 1  # Muutuja i väärtust suurendatakse ühe võrra
#
#exitonclick()

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel2
#from time import sleep
#sisestatud_pin = ""
#katseid = 3
#while sisestatud_pin != "1234" and katseid > 0:
#    print("Sisesta PIN-kood:")
#    print("Jäänud on " + str(katseid) + " katset.")
#    katseid -= 1
#    sisestatud_pin = input()
#if sisestatud_pin == "1234":
#    print("Sisenesid pangaautomaati!")
#else:
#    print("Enesehävitusrežiim aktiveeritud:")
#    i = 10
#    while i > 0:
#        print(i)
#        i -= 1
#        sleep(1)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVTsykkel2
from random import randint

arv = randint(1, 19)  # juhuslik täisarv
print("Mõtlen ühele 20-st väiksemale naturaalarvule. Arva ära!")
arvamus = int(input())

while arvamus != arv:
    if arv > arvamus:
        print("Minu arv on suurem!")
    else:
        print("Minu arv on väiksem!")

    print("Arva veel!")
    arvamus = int(input())

print("Õige! Tubli!")