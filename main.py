import requests, time, csv
from bs4 import BeautifulSoup

products_data = []

for i in range(1, 6):
    res = requests.get(f"https://www.sulakauri.ge/wignebi/?product-page={i}")
    content = res.text

    soup = BeautifulSoup(content, "html.parser")

    products = soup.find_all("li", class_="product")

    for product in products:
        author = product.find("div", class_="mkdf-pl-author-holder").text
        title = product.find("h5").text
        price = product.find("span", class_="woocommerce-Price-amount amount").text
        print(f"{author} - {title} => ფასი: {price}")
        products_data.append([author, title, price])

    print("\n")
    time.sleep(5)


with open("products.csv", "w", encoding="utf-8_sig") as file:
    writer = csv.writer(file)
    writer.writerow(["ავტორი", "სათაური", "ფასი"])

    for product in products_data:
        writer.writerow(product)
