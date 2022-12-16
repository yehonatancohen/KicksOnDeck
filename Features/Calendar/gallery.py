import requests
from bs4 import BeautifulSoup

url = "https://www.nike.com/il/launch?s=upcoming"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
soup.f\

products = []
names = []
product_cards = soup.find_all("div", class_="ncss-col-sm-12 full")[:-1]

for i, product in enumerate(product_cards):
    if i == 0:
        continue
    if i % 2 == 1:
        products.append(product)
    else:
        names.append(product)


for index, product in enumerate(products):
    # Find the name of the shoe
    name = soup.findAll("div", class_="copy-container ta-sm-c bg-white pt6-sm pb7-sm pb7-lg")[index].text.replace("\n"," - ")
    
    # Find the price of the shoe
    #price = product.find("span", class_="product-price__dollars").text

    date = soup.findAll("div", class_="launch-caption ta-sm-c")[index].text.replace("\n"," ")
    
    # Find the image URL of the shoe
    image_url = soup.findAll("div", class_="card-link d-sm-b")[index].findAll("tagName","img").src
    
    print(image_url)
