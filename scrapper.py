# Web Scrape Amazon with Beautiful Soup 📦

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}

def get_product_details(product_url: str) -> dict:
    product_details = {}

    # Ensure URL has scheme
    if not product_url.startswith(("http://", "https://")):
        product_url = "https://" + product_url

    try:
        # Fetch page
        page = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(page.content, "lxml")

        # Title
        title = soup.find('span', attrs={'id': 'productTitle'})
        if title:
            product_details['title'] = title.get_text().strip()

        # Price
        price_whole = soup.find('span', class_="a-price-whole")
        price_symbol = soup.find('span', class_="a-price-symbol")
        if price_whole and price_symbol:
            product_details['price'] = price_symbol.get_text().strip() + price_whole.get_text().strip()

        return product_details

    except Exception as e:
        print("Could not fetch product details")
        print(f"Error: {e}")
        return {}

# Run script
if __name__ == "__main__":
    product_url = input("Enter product url: ")
    product_details = get_product_details(product_url)
    print(product_details)
