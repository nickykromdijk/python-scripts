import random
import re
from collections import defaultdict

print("\nWELKOM BIJ DE RANDOM MEAL PICKER!")
print("-----------------------------------\n")

# Favoriete maaltijden en bijbehorende ingredienten (per persoon)
maaltijden = {
    "Spaghetti Bolognese": [
        "Spaghetti 100g",
        "Gehakt 100g",
        "Tomatensaus 50ml",
        "Ui 0.5 stuks",
        "Knoflook 1 teen",
        "Parmezaanse kaas 20g",
        "Basilicum 5g",
    ],
    "Roti met kip": [
        "Rijst 50g",
        "Kip 100g",
        "Kousenband 50g",
        "Roti 1 stuks",
        "Aardappel 50g",
        "Ui 0.5 stuks",
        "Knoflook 1 teen",
        "Madras kerriepoeder 5g",
        "Zonnebloemolie 10ml",
    ],
    "Zalm met broccoli en rijst": [
        "Rijst 50g",
        "Zalm 100g",
        "Broccoli 50g",
        "Citroen 0.25 stuks",
        "Dille 2g",
    ],
    "Curry met naan": [
        "Curry 100ml",
        "Naan 1 stuks",
        "Kokosmelk 50ml",
        "Kikkererwten 50g",
        "Tomaat 0.5 stuks",
        "Ui 0.5 stuks",
        "Knoflook 1 teen",
        "Gember 5g",
        "Komijnpoeder 5g",
        "Koriander 5g",
    ],
    "Wraps met kip en guacamole": [
        "Wraps 1 stuks",
        "Kip 100g",
        "Avocado 0.5 stuks",
        "Limoen 0.25 stuks",
        "Tomaat 0.5 stuks",
        "Ui 0.5 stuks",
        "Knoflook 1 teen",
        "Koriander 5g",
    ],
    "Boerenkool met worst": [
        "Worst 100g",
        "Aardappelen 150g",
        "Boerenkool 100g",
        "Melk 50ml",
        "Boter 10g",
        "Nootmuskaat 1 snufje",
    ],
    "Lasagne": [
        "Lasagnebladen 50g",
        "Gehakt 100g",
        "Bechamelsaus 50ml",
        "Tomatensaus 50ml",
        "Ui 0.5 stuks",
        "Knoflook 1 teen",
        "Wortel 50g",
        "Parmezaanse kaas 20g",
        "Basilicum 5g",
    ],
    "Pasta pesto": [
        "Pasta 100g",
        "Pesto 30g",
        "Kip 100g",
        "Cherrytomaten 50g",
        "Parmezaanse kaas 20g",
        "Rucola 10g",
    ],
}


def parse_ingredient(ingredient):
    # Haalt de naam en hoeveelheid uit een ingrediënt (bv. 'Kip 100g' → ('Kip', 100, 'g'))
    match = re.match(r"(.+?)\s*(\d*\.?\d*)\s*(g|kg|ml|l|stuks)?$", ingredient)
    if match:
        naam, hoeveelheid, eenheid = match.groups()
        hoeveelheid = float(hoeveelheid) if hoeveelheid else None
        return naam.strip(), hoeveelheid, eenheid or ""
    return ingredient, None, None  # Geen hoeveelheid gevonden


def genereer_weekmenu(aantal_maaltijden, aantal_personen):
    beschikbare_maaltijden = list(maaltijden.keys())
    gekozen_maaltijden = random.sample(
        beschikbare_maaltijden, aantal_maaltijden
    )

    boodschappenlijst = defaultdict(
        lambda: [0, ""]
    )

    for maaltijd in gekozen_maaltijden:
        for item in maaltijden[maaltijd]:
            naam, hoeveelheid, eenheid = parse_ingredient(item)
            if hoeveelheid is not None:
                boodschappenlijst[naam][0] += (
                    hoeveelheid * aantal_personen
                )
                boodschappenlijst[naam][1] = eenheid
            else:
                boodschappenlijst[naam] = [
                    None,
                    "",
                ]  # Ingrediënt zonder hoeveelheid

    # Print het weekmenu
    print("\n📅 Weekmenu:")
    for i, maaltijd in enumerate(gekozen_maaltijden, start=1):
        print(f"{i}. {maaltijd}")

    # Print de boodschappenlijst
    print("\n🛒 Boodschappenlijst:")
    for naam, (totaal_hoeveelheid, eenheid) in sorted(
        boodschappenlijst.items()
    ):
        if totaal_hoeveelheid:
            print(f"- {naam} {totaal_hoeveelheid:.0f} {eenheid}")
        else:
            print(f"- {naam}")


# Start het script
aantal_maaltijden = int(input("Hoeveel maaltijden wil je nu genereren? "))
aantal_personen = int(input("Voor hoeveel personen ga je die maaltijden koken? "))

genereer_weekmenu(aantal_maaltijden, aantal_personen)
