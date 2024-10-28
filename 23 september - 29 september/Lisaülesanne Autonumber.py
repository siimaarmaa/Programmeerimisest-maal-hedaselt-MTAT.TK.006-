import re

# Küsime kasutajalt auto registreerimisnumbri
registreerimisnumber = input("Palun sisesta auto registreerimisnumber: ")

# Määratleme Eesti registreerimisnumbri mustri (3 numbrit ja 3 tähte)
muster = r"^[0-9]{3}[A-Z]{3}$"

# Kontrollime, kas registreerimisnumber vastab mustrile
if re.match(muster, registreerimisnumber):
    print("On Eesti registreerimisnumber")
else:
    print("Ei ole Eesti registreerimisnumber")
