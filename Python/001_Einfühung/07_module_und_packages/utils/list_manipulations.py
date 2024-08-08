def filter_gaesteliste(input_gaesteliste : list):
    gaesteliste = input_gaesteliste.copy()
    gefilterte_gaesteliste = []
    while len(gaesteliste) > 0:
        gast = gaesteliste.pop(0)
        if gast == "Franz":
            continue
        gefilterte_gaesteliste.append(gast)
    return gefilterte_gaesteliste

def funktion2():
    pass
