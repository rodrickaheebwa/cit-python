import requests
from bs4 import BeautifulSoup

def get_cbs_news():
    url = 'https://www.cbsnews.com/latest/rss/main'

    data = requests.get(url)

    soup = BeautifulSoup(data.content, 'lxml')

    items = soup.find_all('item')

    news_items = []

    for item in items:
        title = item.title.text.strip()
        link = item.link.next_sibling.text.strip()
        image = item.image.text.strip()
        description = item.description.text.strip()
        news_items.append({'title' : title, 'link' : link, 'image' : image, 'description' : description})

    return news_items