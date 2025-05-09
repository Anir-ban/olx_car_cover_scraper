import requests
from bs4 import BeautifulSoup

# URL for "car cover" search on OLX
URL = "https://www.olx.in/items/q-car-cover"

# Set headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Send GET request
response = requests.get(URL, headers=HEADERS)

# Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract listing titles (you can extract more like price/location)
    listings = soup.find_all('li', class_='EIR5N')

    with open('olx_car_covers.txt', 'w', encoding='utf-8') as file:
        for item in listings:
            title_tag = item.find('span')
            if title_tag:
                title = title_tag.get_text(strip=True)
                file.write(title + '\n')

    print("Search results saved to 'olx_car_covers.txt'")
else:
    print("Failed to fetch OLX page. Status code:", response.status_code)
