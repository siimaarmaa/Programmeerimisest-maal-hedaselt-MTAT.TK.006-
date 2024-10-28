# Küsime kasutajalt supi algtemperatuuri
supi_algtemperatuur = float(input("Palun sisesta supi algtemperatuur: "))

# Küsime kasutajalt toatemperatuuri
toatemperatuur = float(input("Palun sisesta toatemperatuur: "))

# Supi jahtumise arvutamine 10 minuti jooksul
minutid = 10
temperatuur = supi_algtemperatuur

for _ in range(minutid):
    # Arvutame temperatuuri vähenemise minuti jooksul
    jahtumine = 0.19 * (temperatuur - toatemperatuur)
    # Uuendame temperatuuri
    temperatuur -= jahtumine

# Ümardame tulemuse täisarvuni
lopp_temperatuur = round(temperatuur)

# Väljastame tulemuse
print("Supi temperatuur 10 minuti pärast on: " + str(lopp_temperatuur) + " kraadi")
