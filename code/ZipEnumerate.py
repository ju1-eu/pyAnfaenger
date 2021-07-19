list_a = [10, 20, 30]
list_b = ["Jan", "Peter", "Max"]
list_c = [True, False, True]

# zip (Voraussetzung: gleiche Länge der Listen)
# Ausgabe: Wert
for a, b, c in zip(list_a, list_b, list_c):
    print(a, b, c)
# Ausgabe: index und Wert
for i in range(len(list_a)):
    val = list_a[i]
    print(i, val)
# besser
for i, val in enumerate(list_a):
    print(i, val)
