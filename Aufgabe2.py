from datetime import date, datetime
from doctest import Example
import os

spiegelei = ["Ei", "Salz", "Paprika", "Pfeffer"]
pasta = ["Pasta", "creme fraiche", "Käse", "Spinat", "salz", "Pfeffer"]
salat = ["Salat", "Tomaten", "Gurke", "Olivenöl"]


def Rezept():
    rezept = int(
        input(
            "welches Rezept ausgegeben werden soll 1. Spiegelei 2. Pasta 3. Salat   :"
        )
    )
    if rezept == 1:
        print(f"Die Zutaten für Spiegelei sind: {spiegelei}")
    elif rezept == 2:
        print(f"Die Zutaten für Pasta sind: {pasta}")
    elif rezept == 3:
        print(f"Die Zutaten für Salat sind: {salat}")
    else:
        print("Ungültige Auswahl! Bitte gib 1, 2 oder 3 ein.")


def weekday_after(weekday, days):
    wochentag = [
        "montag",
        "dienstag",
        "mittwoch",
        "donnerstag",
        "freitag",
        "samstag",
        "sonntag",
    ]
    nb = len(wochentag)
    for i in range(nb):
        # print(wochentag[i].index(weekday))
        if weekday == wochentag[i]:
            tag_resut = i + days
            print(f"weekday : {wochentag[tag_resut]}")


# Rezept()

# tag = input("einen Wochentag Eingeben: ")
# zahl = int(input("eine Zahl eingeben: "))
# weekday_after(tag.lower(), zahl)


def anzahl_worte(name_file):

    if os.path.exists(name_file) and name_file.endswith(".txt"):
        with open(name_file, "r") as file:
            # Lese den Inhalt der Datei
            inhalt = file.read()
            print("Inhalt der Datei:")
            print(inhalt)

            # Berechne die Anzahl der Worte
            wortanzahl = len(inhalt.split())
            print(f"Anzahl der Wörter in der Datei: {wortanzahl}")
    else:
        print("Die Datei existiert nicht oder ist keine .txt-Datei!")


file_name = "Example.txt"
anzahl_worte(file_name)
