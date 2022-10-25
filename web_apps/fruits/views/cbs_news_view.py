from flask import Blueprint
import requests
from bs4 import BeautifulSoup
from fruits.models import CbsNews

cbsviews = Blueprint('cbsviews', __name__, url_prefix='/cbs_news')

def get_cbs_news():
    url = 'https://www.cbsnews.com/latest/rss/main'

    data = requests.get(url)

    soup = BeautifulSoup(data.content, features='xml')

    items = soup.find_all('item')

    news_items = []

    for item in items:
        title = item.title.text.strip()
        link = item.link.next_sibling.text.strip()
        image = item.image.text.strip()
        description = item.description.text.strip()
        news_items.append({'title' : title, 'link' : link, 'image' : image, 'description' : description})

    return news_items

@cbsviews.route('/')
def cbs_news():
    news_articles = get_cbs_news() # new data
    data = CbsNews.get_all_news() # existing data
    
    # loop through articles
    for news in news_articles:
        # check if news already exists in database
        if news.get('title').lower() not in [info.title.lower() for info in data]:
            row = CbsNews(title = news['title'], link = news['link'], description = news['description'], image = news['image'])
            row.save()
        else:
            continue

    return {'data': [news.serialize() for news in data]}