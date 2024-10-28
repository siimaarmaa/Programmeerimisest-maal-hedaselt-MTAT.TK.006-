def laeva_teekond(kiirus_solmedes):
    # Arvutame teekonna kilomeetrites ja ümardame täisarvuni
    teekond_kilomeetrites = round(kiirus_solmedes * 1852 / 1000 * 24)
    return teekond_kilomeetrites

# Küsime kasutajalt laeva kiiruse sõlmedes
kiirus = int(input("Palun sisesta laeva kiirus sõlmedes: "))

# Kasutame laeva_teekond funktsiooni teekonna arvutamiseks
teekond = laeva_teekond(kiirus)

# Väljastame tulemuse
print("Laeva teekond ööpäevas on:", teekond, "kilomeetrit")
