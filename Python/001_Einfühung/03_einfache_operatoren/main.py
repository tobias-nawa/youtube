# 	•	Arithmetische Operatoren: +, -, *, /, %
#	•	Vergleichsoperatoren: ==, !=, >, <
#	•	Logische Operatoren: and, or, not

zieltemperatur = 90 + 1
print("Zieltemperatur:", zieltemperatur)

aktuelle_temperatur = 100

if aktuelle_temperatur >= zieltemperatur and \
    not(aktuelle_temperatur >= 100):
    print("FERTIG!")
    print("Temperatur erreicht.")
elif aktuelle_temperatur >= 100:
    print("Temperatur zu hoch")
print("Ende")
