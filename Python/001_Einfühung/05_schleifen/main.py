meine_gaeste = ["Peter", "Franz", "Martin", "Stefan"]

for gast in meine_gaeste:
    print("-", gast)

print(meine_gaeste)

for index in range(4):
    print(index,": Sekt für:", meine_gaeste[index])

print(meine_gaeste)

counter = 0
while len(meine_gaeste) > 0:
    gast = meine_gaeste.pop(0)
    if gast == "Franz":
        continue
    print("-", gast)
    counter += 1
    if counter == 2:
        break

print("Ende")