# Funktion: max
def list_max(my_list):
    result = my_list[0]
    for i in range(1, len(my_list)):
        wert = my_list[i]
        if wert > result:
            result = wert
    return result


# Liste
l1 = [-2, 1, -10]
l2 = [-20, 123, 22]

# Funktionsaufruf
l1_max = list_max(l1)
l2_max = list_max(l2)
