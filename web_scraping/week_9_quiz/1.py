# Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order.

import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.imdb.com/list/ls000578090/"

page = requests.get(base_url)

soup = BeautifulSoup(page.content, 'html.parser')

item_list = soup.find(class_ = 'lister-list')

items = item_list.find_all(class_ = 'lister-item')

movies = []

for item in items:
    data = item.find(class_ = 'lister-item-content')

    def get_actors_directors():
        elem = data.find_all('p', class_ = 'text-small')[1]
        directors, actors = elem.text.strip().split('|')
        directors = directors.replace('\n', ' ').split(',')
        actors = actors.replace('\n', ' ').split(',')
        new_directors = []
        new_actors = []
        for director in directors:
            if ':' in director:
                new_directors.append(director.split(':')[1].strip())
            else:
                new_directors.append(director.strip())

        for actor in actors:
            if ':' in actor:
                new_actors.append(actor.split(':')[1].strip())
            else:
                new_actors.append(actor.strip())
        return new_directors, new_actors

    title = data.find(class_ = 'lister-item-header').find('a').text.strip()
    year = data.find(class_ = 'lister-item-year').text.strip().strip('()')
    try:
        rating = float(data.find(class_ = 'ipl-rating-star__rating').text.strip())
    except:
        rating = 'not available'
    try:
        metascore = data.find(class_ = 'ratings-metascore').find('span').text.strip()
    except:
        metascore = 'not available'
    try:
        votes = data.find('span', text = 'Votes:').next_sibling.next_sibling.text.strip()
    except:
        votes = 'not available'
    try:
        gross = data.find('span', text = 'Gross:').next_sibling.next_sibling.text.strip()
    except:
        gross = 'not available'
    directors, actors = get_actors_directors()
    runtime = data.find(class_ = 'runtime').text.strip()
    genre = data.find(class_ = 'genre').text.strip()
    description = data.find_all('p')[1].text.strip()

    movies.append({
        'title' : title, 'year' : year, 'rating' : rating, 'metascore' : metascore, 'votes' : votes, 'gross' : gross, 'runtime' : runtime, 'genre' : genre, 'directors' : directors, 'actors' : actors, 'description' : description
    })

movies = sorted(movies, key = lambda x : x['rating'], reverse=True)

with open('movies.csv', mode='w') as movies_file:
    movie_writer = csv.writer(movies_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for movie in movies:
        movie_writer.writerow([movie['title'], movie['year'], movie['rating'], movie['metascore'], movie['votes'], movie['gross'], movie['directors'], movie['actors'], movie['runtime'], movie['runtime'], movie['genre']])