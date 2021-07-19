# Liste
names = ["Ben", "Jan", "Peter", "Melissa"]
noten = [1, 2, 1, 4]

# dict {(key, value)}
names_and_noten = {"Ben": 1, "Jan": 2, "Peter": 1, "Melissa": 4}

# Wert hinzufügen
names_and_noten.update({"Pia": 3})
# oder
names_and_noten["Julia"] = 1
# Wert entfernen
names_and_noten.pop("Julia")

# Keys
for k in names_and_noten.keys():
    print(k)
# Values = Werte
for v in names_and_noten.values():
    print(v)
# Keys und Values
for k, v in names_and_noten.items():
    print(k, v)

# Ist Key vorhanden?
if "Julia" in names_and_noten:
    present = True
else:
    present = False
