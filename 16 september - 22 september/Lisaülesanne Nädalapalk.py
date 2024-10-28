# Küsime kasutajalt töötundide arvu nädalas
tootunnid = float(input("Palun sisesta töötundide arv nädalas: "))

# Küsime kasutajalt tavalise tunnitasu
tunnitasu = float(input("Palun sisesta tavaline tunnitasu: "))

# Arvutame nädala palga
if tootunnid <= 40:
    # Kui töötundide arv on 40 või vähem, siis arvutame tavalise palga
    nadalapalk = tootunnid * tunnitasu
else:
    # Kui töötundide arv on üle 40, arvutame ületundide palga
    tavaliselt_tunnid = 40
    uletunnid = tootunnid - 40
    uletundide_tasu = tunnitasu * 1.5

    nadalapalk = (tavaliselt_tunnid * tunnitasu) + (uletunnid * uletundide_tasu)

# Väljastame nädala palga
print("Teie nädala palk on: " + str(nadalapalk) + " eurot")
