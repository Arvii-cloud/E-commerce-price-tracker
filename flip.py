import requests
from bs4 import BeautifulSoup
from email_alert import alert_system  
URL ="https://www.flipkart.com/boult-astra-quad-mic-enc-48hrs-battery-low-latency-gaming-made-india-5-3v-bluetooth/p/itmd2008f28b12bd?pid=ACCGS2VSKG3E2JW8&lid=LSTACCGS2VSKG3E2JW8GGXDAU&marketplace=FLIPKART&store=0pm%2Ffcn&srno=b_1_1&otracker=browse&fm=organic&iid=en_0mx6zFUcMUypPAzKR_rVp2LVl137dZAbwXnFpR6V19Alb6tY3t6MVmGu3EpeNkan_ngZYz3xphDXXqrrrP2EwQ%3D%3D&ppt=hp&ppn=homepage&ssid=59vg9khu740000001748165860999"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}
set_price=2000
def check_price():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    title_tag = soup.find("span", {"class": "VU-ZEz"})
    price_tag = soup.find("div", {"class": "Nx9bqj CxhGGd"})

    if title_tag and price_tag:
        product_title = title_tag.get_text().strip()
        price_text = price_tag.get_text().strip().replace("₹", "").replace(",", "")
        price_number = float(price_text)

        print(f"Current price: ₹{price_number}")

        if price_number <= set_price:
            alert_system(product_title, URL)
            print("Alert sent!")
        else:
            print("Price is still high.")
    else:
        print("Product info not found. Check selectors or page structure.")

check_price()