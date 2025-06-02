try:
    import requests
except ImportError:
    print("Je mist een stukje dat nodig is voor dit script: 'requests'.")
    print("Open een terminal en voer dit uit: pip install requests")
    print("Meer informatie in de README.md")
    exit(1)
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Je mist een stukje dat nodig is voor dit script: 'beautifulsoup4'.")
    print("Open een terminal en voer dit uit: pip install beautifulsoup4")
    print("Meer informatie in de README.md")
    exit(1)
import re

print("\nWELKOM BIJ DE LOAVIES PRODUCT SALE CHECKER!")
print("------------------------------------------\n")
print("Het script begint nu met het checken van de items...\n")

# Lees de productlinkjes uit het bestand in de input folder
with open("input/product_linkjes.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file if line.strip()]

# Headers om blokkades te vermijden
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def extract_price(price_text):
    """Haal alleen het numerieke deel van de prijs op en converteer naar float."""
    price_match = re.search(r"(\d+,\d+)", price_text)
    if price_match:
        return float(price_match.group(1).replace(",", "."))
    return None


def check_sale(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
    except requests.RequestException as e:
        print(f"⚠️ Fout bij het ophalen van {url}: {e}")
        return 0

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        original_price_element = soup.select_one("span.product-price")
        original_price = (
            extract_price(original_price_element.get_text(strip=True))
            if original_price_element
            else None
        )

        discount_label = soup.select_one("span.discount-label")
        discount_percentage = None

        if discount_label:
            discount_text = discount_label.get_text(strip=True)
            discount_match = re.search(r"-(\d+)%", discount_text)
            if discount_match:
                discount_percentage = int(discount_match.group(1))

        if original_price and discount_percentage:
            current_price = round(original_price * (1 - discount_percentage / 100), 2)
            print(f"🎉 SALE op item met link {url} met {discount_percentage}% korting!")
            print(f"Originele prijs: €{original_price}")
            print(f"Nu te koop voor: €{current_price}\n")
            return 1
        else:
            print(
                f"Geen korting op item met link {url}. Normale prijs: €{original_price}\n"
            )
            return 0
    else:
        print(f"⚠️ Fout bij het laden van de pagina ({response.status_code}) van item {url}\n")
        return 0


# Doorloop alle links en check de sale
aantal_sale_items = 0


for url in urls:
    aantal_sale_items += check_sale(url)

print(
    "Aantal items uit jouw product_linkjes.txt bestand in de sale: ",
    aantal_sale_items,
)
