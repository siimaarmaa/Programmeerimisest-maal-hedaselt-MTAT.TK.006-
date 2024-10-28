import re

# Küsime kasutajalt isikukoodi
isikukood = input("Palun sisesta isikukood: ")

# Määratleme Eesti isikukoodi mustri
muster = r"^[1-6][0-9]{10}$"

# Kontrollime, kas isikukood vastab mustrile
if re.match(muster, isikukood):
    print("On Eesti isikukood")
else:
    print("Ei ole Eesti isikukood")
