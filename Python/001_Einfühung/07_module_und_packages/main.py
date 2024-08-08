from utils.list_manipulations import filter_gaesteliste, funktion2
from utils.text_manipulations import funktion3

meine_gaeste = ["Peter", "Franz", "Martin", "Stefan"]

neue_gaesteliste = filter_gaesteliste(meine_gaeste)
print("Neu:", neue_gaesteliste)
print("Alt:", meine_gaeste)

liste2 = ["a", "b", "c"]
neue_liste2 = filter_gaesteliste(liste2)
print(liste2)

funktion2()
funktion3()