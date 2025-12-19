from bs4 import BeautifulSoup
import  requests
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv(".env")

HEADERS: dict = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,/;q=0.8',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Dnt': '1',
'Priority': 'u=1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrage-Insecure-Requests': '1',
}



static_site="https://appbrewery.github.io/instant_pot/"
live_site="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response=requests.get(live_site,headers=HEADERS)
print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
web_price=float(soup.find(name="span",class_="a-offscreen").get_text().split('$')[1])
raw_title = soup.find(name="span", id="productTitle").get_text()

product_title = " ".join(raw_title.split())  # collapse multiple spaces/newlines into single spaces
print(product_title)

my_email=os.getenv("email")
passw=os.getenv("pass")
to_email=os.getenv("to_email")
target=100.00

if web_price < target:
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passw)

            msg = EmailMessage()
            msg["From"] = my_email
            msg["To"] = to_email
            msg["Subject"] = f"Price drop: {product_title}"
            # set_content handles proper UTF-8 encoding
            msg.set_content(f"{product_title} is now ${web_price:.2f}")

            connection.send_message(msg)

            print("Email has been sent")
    except Exception as e:
        print(e)
