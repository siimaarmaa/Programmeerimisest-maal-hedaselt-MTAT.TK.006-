def netopalk(brutopalk):
    maksuvaba_minimum = 170
    tulumaksumaar = 0.20

    if brutopalk <= maksuvaba_minimum:
        netopalk = brutopalk
    else:
        maksustatav_osa = brutopalk - maksuvaba_minimum
        tulumaks = maksustatav_osa * tulumaksumaar
        netopalk = brutopalk - tulumaks

    return round(netopalk, 2)


# Küsime kasutajalt isa brutopalga
isa_brutopalk = float(input("Palun sisesta isa brutopalk: "))

# Küsime kasutajalt ema brutopalga
ema_brutopalk = float(input("Palun sisesta ema brutopalk: "))

# Küsime kasutajalt alaealiste laste arvu
alaealiste_laste_arv = int(input("Palun sisesta alaealiste laste arv: "))

# Arvutame isa ja ema netopalga
isa_netopalk = netopalk(isa_brutopalk)
ema_netopalk = netopalk(ema_brutopalk)

# Arvutame laste toetuse
laste_toetus = alaealiste_laste_arv * 50

# Arvutame pere kuusissetuleku
pere_sissetulek = isa_netopalk + ema_netopalk + laste_toetus

# Ümardame tulemuse 2 komakohani
pere_sissetulek = round(pere_sissetulek, 2)

# Väljastame tulemuse
print("Pere kuusissetulek on:", pere_sissetulek, "eurot")
