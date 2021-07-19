# Funktion: max
def list_max(my_list):
    result = my_list[0]
    for i in range(1, len(my_list)):
        wert = my_list[i]
        if wert > result:
            result = wert
    return result
