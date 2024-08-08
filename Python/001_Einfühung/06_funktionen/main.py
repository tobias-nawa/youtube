meine_gaeste = ["Peter", "Franz", "Martin", "Stefan"]

def filter_gaesteliste(input_gaesteliste : list):
    gaesteliste = input_gaesteliste.copy()
    gefilterte_gaesteliste = []
    while len(gaesteliste) > 0:
        gast = gaesteliste.pop(0)
        if gast == "Franz":
            continue
        gefilterte_gaesteliste.append(gast)
    return gefilterte_gaesteliste

neue_gaesteliste = filter_gaesteliste(meine_gaeste)
print("Neu:", neue_gaesteliste)
print("Alt:", meine_gaeste)

liste2 = ["a", "b", "c"]
neue_liste2 = filter_gaesteliste(liste2)
print(liste2)