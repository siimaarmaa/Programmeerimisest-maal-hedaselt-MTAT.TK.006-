# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon1
#def trükiAB():
#    print("A")
#    print("B")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon1
#def trükiAB():
#    print("A")
#    print("B")
#
#print("C")
#trükiAB()
#print("D")
#trükiAB()

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon1
#def funktsioon():
#    a = 1
#    b = 4
#    print(a + b)
#print(41)
#funktsioon()

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon1
#trükiAB()
#def trükiAB():
#    print("A")
#    print("B")

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon1
#def funktsioon_a():
#    print("a")
#def funktsioon_b():
#    funktsioon_a()
#    print("b")
#funktsioon_b()
#funktsioon_a()

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon2
#from time import sleep
#def loe_alla(i):
#    while i > 0:
#        i -= 1
#        print(i)
#        sleep(1)
#
#loe_alla(6)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon2
#def ruutu(x):
#   return x**2
#print(ruutu(4))

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon2
#def reaktsioon(punkte):
#    if punkte >= 50:
#        return "Olid tubli!"
#    else:
#        return "Püüa veel!"
#print(reaktsioon(50))

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon2
#def summa(x,y):
#    return x + y
#
#a = 4
#b = 5
#print(summa(a,b))

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIFunktsioon2
#def summa(x,y):
#    return x + y
#a = summa(summa(1,3)*2, 4)
#print(a)

# https://courses.cs.ut.ee/2024/progmaa/fall/Main/PARTVIIIFailid
from urllib.request import urlopen

vastus = urlopen("https://kodu.ut.ee/~marinai/maa.txt")

baidid = vastus.read()
# veebist lugemisel annab käsk read() meile tavalise sõne asemel hunniku baite,
# mis on vaja veel sõneks "dekodeerida"
tekst = baidid.decode()
vastus.close()

print(tekst[10].upper() + tekst[2] + tekst[-2])