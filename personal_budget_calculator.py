print("\nWELKOM BIJ DE PERSOONLIJKE BUDGET CALCULATOR!")
print("-----------------------------------\n")

netto_salaris = float(input("Wat is je netto salaris (in €)? "))

vaste_laten_percentage = 50
investeren_percenage = 12.5
aflossen_percentage = 0
sparen_percentage = 7.5
vrije_tijd = 30

hebt_schulden = input("Heb je schulden? (ja/nee): ").strip().lower()

if hebt_schulden == "ja":
    rente_hoog = input("Is de rente hoger dan 3,5%? (ja/nee): ").strip().lower()
    if rente_hoog == "ja":
        print("\nAdvies: Aflossen is belangrijker dan investeren op dit moment.")
        investeren_percenage = 4
        aflossen_percentage = 10
        sparen_percentage = 6
    else:
        aflossen_percentage = 0


print("\nJe budgetverdeling:")
print(f"Vaste lasten: €{netto_salaris * (vaste_laten_percentage/100):.2f}")

if aflossen_percentage > 0:
    print(f"Aflossen: €{netto_salaris * (aflossen_percentage/100):.2f}")
    print(f"Investeren: €{netto_salaris * (investeren_percenage/100):.2f}")

else:
    print(f"Investeren: €{netto_salaris * (investeren_percenage/100):.2f}")

print(f"Sparen: €{netto_salaris * (sparen_percentage/100):.2f}")
print(f"Vrije tijd: €{netto_salaris * (vrije_tijd/100):.2f}")
