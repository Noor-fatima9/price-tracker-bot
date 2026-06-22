from bs4 import BeautifulSoup
import requests

print("Script started...")

URL = "https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

try:
    print("Fetching data from Amazon...")
    page = requests.get(URL, headers=headers, timeout=10)
    print("Response received. Status code:", page.status_code)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle")
    
    if title:
        print("Product:", title.get_text().strip())
    else:
        print("Title not found. Amazon might have changed the HTML structure.")
        
    price = soup.find('span', 'a-price-whole')
    if price:
        print("Price: $", price.get_text())
    else:
        print("Price not found.")
        
except Exception as e:
    print("An error occurred:", e)

print("Script finished.")