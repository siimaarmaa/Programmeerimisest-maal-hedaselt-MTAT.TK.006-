punktid = 0
tase = 5
while tase > 0:
    punktid += tase
    tase -= 1
print(punktid)

i = 1
a = 0
while i <= 10:
    if i % 2 == 0:
        a += 1
    i = i + 1
print(a)

arv = 2
arv **= 11
print(arv)

#from turtle import *
#kulg = 0
#while kulg < 6:
#    forward(100)
#    left(120)
#    kulg = kulg + 1
#exitonclick()

import re
sona = "ot0hoo"
avaldis = "t[0-9][a-z]"
if re.search(avaldis, sona):
    print("Leiti")
else:
    print("Ei leitud")