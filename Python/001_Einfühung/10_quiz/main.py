from halo import Halo
from time import sleep

def quiz_game():
    fragen = {
        "Was ist die Hauptstadt von Deutschland?": "Berlin",
        "Wie viele Planeten gibt es im Sonnensystem?": "8",
        "Was ist die größte Wüste der Welt?": "Antarktis",
        "Welches Element hat das chemische Symbol 'O'?": "Sauerstoff"
    }

    print("Willkommen zum Quiz-Spiel!")
    score = 0

    for frage, richtige_antwort in fragen.items():
        antwort = input(frage + " ")

        spinner = Halo("Überprüfe die Antwort", spinner="dots")
        spinner.start()
        sleep(2)
        spinner.stop()

        if antwort.strip().lower() == richtige_antwort.lower():
            print("Richtig!")
            score += 1
        else:
            print(f"Leider falsch! Die richtige Antwort ist {richtige_antwort}.")

    print(f"Du hast {score} von {len(fragen)} Fragen richtig beantwortet.")

quiz_game()

