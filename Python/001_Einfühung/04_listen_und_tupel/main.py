meine_gaeste = ["Peter", "Franz", "Martin"]

print(meine_gaeste)

meine_gaeste.append("Stefan")

print(meine_gaeste)

meine_gaeste.pop()

print(meine_gaeste)

entfernter_gast = meine_gaeste.pop(0)
print(meine_gaeste)
print(entfernter_gast)

meine_gaeste[0] = "Franz der 2te"
print(meine_gaeste)

mein_tupel = (1, 2)
print(mein_tupel[0:2])

mein_tupel = (1, 2, 3, 2, 1)
print(mein_tupel.count(3))
