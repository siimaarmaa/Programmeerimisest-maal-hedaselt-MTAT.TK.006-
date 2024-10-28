# Küsime kasutajalt kandiku laiuse küpsistes
laiuse_küpsised = int(input("Mitu küpsist mahub kandikule laiuses (küpsistes)? "))

# Küsime kasutajalt kandiku pikkuse küpsistes
pikkuse_küpsised = int(input("Mitu küpsist mahub kandikule pikkuses (küpsistes)? "))

# Küsime kasutajalt kihtide arvu
kihid = int(input("Mitu kihti soovite teha? "))

# Küsime kasutajalt, kui palju küpsiseid on ühes pakis
küpsised_pakis = int(input("Kui mitu küpsist on ühes pakis? "))

# Arvutame, kui palju küpsiseid on vaja kogu tordi jaoks
kogu_küpsised = laiuse_küpsised * pikkuse_küpsised * kihid

# Arvutame, kui palju küpsiste pakke on vaja
pakke_vaja = kogu_küpsised / küpsised_pakis

# Kui pakke_vaja pole täisarv, ümardame üles
pakke_vaja = int(pakke_vaja) if kogu_küpsised % küpsised_pakis == 0 else int(pakke_vaja) + 1

print(f"Kogu tordi jaoks on vaja {kogu_küpsised} küpsist.")
print(f"Küpsiste pakkide arv, mida on vaja: {pakke_vaja}")
