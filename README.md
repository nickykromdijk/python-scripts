

# 🐍 Simpele Python-scripts voor beginners

Welkom! In deze map vind je leuke Python-scripts die (soms) dingen doen met data uit de `input`-folder.

Deze scripts zijn bedoeld voor mensen die net beginnen met programmeren. Je hebt geen ervaring nodig! Lees goed deze handleiding.

## Wat heb je nodig?

### 1. De scripts

1. Je kunt de scripts (`.py` bestanden) downloaden door er op te klikken en dan rechtsbovenin op het Download knopje te drukken. Ik raad je aan om met de `weekly_meal_planner.py` of de `personal_budget_calculator.py` te beginnen.

2. Later kun je ook het bestand in de input folder downloaden en dan zelf in een nieuw mapje genaamd `input` op jouw computer stoppen. De input folder en de scripts moeten op dezelfde locatie staan.


### 2. Python installeren

Heb je nog geen Python op je computer?

➡️ Ga naar: [https://www.python.org/downloads](https://www.python.org/downloads)

Klik op de knop **“Download Python”** en volg de stappen om het te installeren.

**Let op**: vink tijdens de installatie aan: **"Add Python to PATH"** (heel belangrijk!).

Bij Python zit standaard ook het programma **IDLE** (Integrated Development and Learning Environment). Dat gaan we gebruiken!


## Script uivoeren

### Aanbevolen manier voor beginners: uitvoeren via IDLE (supermakkelijk)

1. Open **IDLE** (Zoek naar “IDLE” op je computer via Start, Spotlight of Zoeken)

2. In IDLE, klik bovenin op **File > Open...** Zoek het Python script (`.py` bestand) dat je wilt uitvoeren, bijvoorbeeld: `weekly_meal_planner.py` die waarschijnlijk in je Downloads staat.

3. Het script opent nu in een apart venster. Klik op **Run > Run Module** of druk op **F5** om het script uit te voeren. Je ziet nu de output van het script in een nieuw wit venster (de Python Shell).

4. Wil je het script opnieuw uitvoeren? Herhaal dan stap 3. Let op: doe dit in het script, niet in het in nieuwe venster met de output (de Python Shell).



### Alternatieve manier: via de terminal (voor wie al wat ervaring heeft)

Als je al een code editor gebruikt (zoals VS Code), of gewend bent aan de terminal, kun je het script ook zo uitvoeren:

1. Open een terminal of opdrachtprompt

2. Voer dit commando uit:

```bash

python  pad/naar/python-scripts/loavies_sale_checker.py

```

## Extra uitleg voor `loavies_sale_checker.py` (gevorderd)
De meeste scripts in deze map kun je zo gebruiken zonder iets extra’s te installeren. Maar er is één scriptje dat een beetje extra uitleg nodig heeft:
`loavies_sale_checker.py`

Dit script bekijkt of producten in de aanbieding zijn bij de webshop Loavies. Hiervoor moet het verbinden met internet en een webpagina uitlezen, en dat kan alleen als Python daar wat extra hulp bij krijgt van twee “hulpmiddelen” (die noemen we libraries).

### Stap 1. Extra libraries installeren (via de terminal)

Voor dit script heb je iets nodig dat niet standaard in Python zit. Gelukkig kun je dat heel makkelijk installeren met één regel code.

1.  Open een terminal of opdrachtprompt (op Windows: zoek op 'Opdrachtprompt' of 'Command promp', op Mac: gebruik Spotlight en typ 'Terminal')

2.  Typ dan dit commando in en druk op enter:
```bash
pip install requests beautifulsoup4
```

### Stap 2: Input-folder
Dit script gebruikt een tekstbestandje met linkjes van producten. Zorg dat je in dezelfde map als waar het `loavies_sale_checker.py` script staat een mapje maakt met de naam `input`, en daarin het bestandje genaamd `product_linkjes.txt` stopt.  📄 Die kun je downloaden uit de input-folder hier op GitHub.

Zorg dat de `input`-map op dezelfde locatie staat als het script.

### Stap 3: Uitvoeren
Je kunt dit script ook openen in IDLE en uitvoeren met **Run > Run Module** of via de terminal (zoals hierboven uitgelegd bij “Script uitvoeren”).


## Tips

- Krijg je een foutmelding? Geen paniek, dat is normaal. Lees goed wat er staat.
- Probeer stap voor stap te ontdekken wat elk script doet.
- Gewoon proberen = leren!

Kom je er niet uit? Stuur me dan een DM op Instagram naar @codewithnicky of stuur een e-mail naar nicky@nkacademy.nl


Veel plezier met Python! 🐍🎉