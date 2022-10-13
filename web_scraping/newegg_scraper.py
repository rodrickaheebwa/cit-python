import requests
from bs4 import BeautifulSoup
import json

# search_term = 'mac book'
search_term = input("What product do you want to search for? : ")

# base_url = f"https://www.newegg.ca/p/pl?d={search_term.replace(' ', '+')}"
base_url = f"https://www.newegg.ca/p/pl?d={search_term}"

page = requests.get(base_url)

doc = BeautifulSoup(page.content, 'html.parser')

# product_div = doc.find_all('div', class_ = 'item-cells-wrap')

page_number_text = doc.find(class_ = 'list-tool-pagination-text').strong
# pages = int(str(page_number_text).split('/')[-2].split('<')[-2][-2:])
# pages = int(page_number_text.text[-2:])
pages = int(page_number_text.text.split('/')[1])

items_found = {}

for page in range(1,pages+1):
    url = f"{base_url}&page={page}"
    html_page = requests.get(url)
    doc = BeautifulSoup(html_page.content, 'html.parser')

    # product_div = doc.find_all('div', class_ = 'item-cells-wrap')
    items = doc.find_all(class_ = 'item-cell')

    for index, item in enumerate(items):
        # product = item.find(class_ = 'item-info').find('a')
        # product_name = product.text
        # product_link = product['href']
        # product_price = item.find(class_ = 'price-current').strong.text

        product_name = item.find(class_ = 'item-title').text
        product_link = item.find(class_ = 'item-title')['href']
        try:
            product_price = item.find(class_ = 'price-current').strong.text
        except:
            product_price = 'price not available'
        product_image = item.find('img').get('src')

        key = f"page{page}-item{index+1}"

        items_found[key] = {
            "product_name": product_name,
            "price": int(product_price.replace(",", '')),
            "image": product_image,
            "link": product_link}

        print('Product Name : ', product_name)
        print('Product Link : ', product_link)
        print('Product Price : ', product_price)
        print('Product image : ', product_image)
        print('\n')
        break

    # print('\n\n')

items_found = sorted(items_found.items(), key = lambda x: x[1]["price"])
items_found = dict(items_found)

with open("items.json", "w") as file:
    json.dump(items_found, file, indent=4)