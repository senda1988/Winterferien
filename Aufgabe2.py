spiegelei = ["Ei", "Salz", "Paprika", "Pfeffer"]
pasta = ["Pasta", "creme fraiche", "Käse", "Spinat", "salz", "Pfeffer"]
salat = ["Salat", "Tomaten", "Gurke", "Olivenöl"]


def Rezept():
    rezept = int(
        input("welches Rezept ausgegeben werden soll 1. Spiegelei 2. Pasta 3. Salat")
    )
    if rezept == 1:
        print(f"Die Zutaten für Spiegelei sind: {spiegelei}")
    elif rezept == 2:
        print(f"Die Zutaten für Pasta sind: {pasta}")
    elif rezept == 3:
        print(f"Die Zutaten für Salat sind: {salat}")


Rezept()
