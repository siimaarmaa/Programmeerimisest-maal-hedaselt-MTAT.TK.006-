# Küsime kasutajalt ridade arvu
ridade_arv = int(input("Palun sisesta ridade arv: "))

# Algne palkide summa on 0
summa = 0

# Kasutame loendurit, mis alustab väärtusest 1
i = 1

# Kontrollime, et sisestatud ridade arv on positiivne
if ridade_arv > 0:
    # While-tsükkel, mis kestab kuni loendur on väiksem või võrdne ridade arvuga
    while i <= ridade_arv:
        # Lisame loenduri väärtuse summale
        summa += i
        # Suurendame loenduri väärtust 1 võrra
        i += 1
else:
    summa = 0

# Väljastame tulemuse
print("Virnas olevate palkide arv on: " + str(summa))
