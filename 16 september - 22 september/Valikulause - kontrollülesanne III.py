# Küsimine kasutajalt
isikukood = input("Sisesta isikukood: ")

# Kontrollime, kas esimene number vastab mehele või naisele
if isikukood[0] == '1' or isikukood[0] == '3' or isikukood[0] == '5':
    sugu = "He"
elif isikukood[0] == '2' or isikukood[0] == '4' or isikukood[0] == '6':
    sugu = "She"
else:
    sugu = "Sugu pole tuvastav"

print(sugu)
