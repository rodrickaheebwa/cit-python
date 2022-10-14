# Scrap Hacker News project and save the result in a csv file. The csv file should have the following columns: title, link, points, comments, author, rank. The csv file should be sorted by rank in ascending order.

import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://news.ycombinator.com/"

page = requests.get(base_url)

soup = BeautifulSoup(page.content, 'html.parser')

item_list = soup.find(class_ = 'itemlist')

items_1 = item_list.find_all(class_ = 'athing')
items_2 = item_list.find_all(class_ = 'subline')

articles = []

for i in range(len(items_1)):
    title = items_1[i].find(class_ = 'titleline').find('a').text.strip()
    link = items_1[i].find(class_ = 'titleline').find('a')['href'].strip()
    rank = int(items_1[i].find(class_ = 'rank').text.strip().strip('.'))
    points = items_2[i].find(class_ = 'score').text.strip()
    comments = items_2[i].find(string=lambda text : 'comments' in text.lower())
    author = items_2[i].find(class_ = 'hnuser').text.strip()

    articles.append({
        'rank' : rank,
        'title' : title,
        'link' : link,
        'points' : points,
        'comments' : comments,
        'author' : author
    })

articles = sorted(articles, key = lambda x : x['rank'])

with open('articles.csv', mode='w') as articles_file:
    article_writer = csv.writer(articles_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for article in articles:
        article_writer.writerow([article['rank'], article['title'], article['link'], article['points'], article['author'], article['comments']])