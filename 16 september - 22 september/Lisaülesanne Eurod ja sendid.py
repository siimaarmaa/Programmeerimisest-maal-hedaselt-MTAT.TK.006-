# Küsime kasutajalt sente
sente = int(input("Palun sisesta arv sente: "))

# Arvutame täiseurod ja ülejäänud sendid
eurod = sente // 100
ulejaanud_sendid = sente % 100

# Koostame väljundi
if eurod > 0 and ulejaanud_sendid > 0:
    if eurod == 1 and ulejaanud_sendid == 1:
        result = f"{eurod} euro ja {ulejaanud_sendid} sent"
    elif eurod == 1:
        result = f"{eurod} euro ja {ulejaanud_sendid} senti"
    elif ulejaanud_sendid == 1:
        result = f"{eurod} eurot ja {ulejaanud_sendid} sent"
    else:
        result = f"{eurod} eurot ja {ulejaanud_sendid} senti"
elif eurod > 0:
    if eurod == 1:
        result = f"{eurod} euro"
    else:
        result = f"{eurod} eurot"
else:
    if ulejaanud_sendid == 1:
        result = f"{ulejaanud_sendid} sent"
    else:
        result = f"{ulejaanud_sendid} senti"

# Väljastame tulemuse
print(result)
