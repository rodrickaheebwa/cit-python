# python -m http.server -- to boot up an http server

# 1. Having an html string and want to get data from it.
# 2. Reading from an html file
# 3. Scraping from an online webpage

import requests
from bs4 import BeautifulSoup

html_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>Web Scraping</h1>
        <p>Web scraping is a technique to automatically access and extract large amounts of information from a website, which can save a huge amount of time and effort.</p>
        <p>Web scraping can be done manually through a web browser. However, this process is both time-consuming and error-prone. Fortunately, there are several web scraping tools that can help you automate the process.</p>
        <p>Web scraping tools can be used to extract data from websites and save it to a local file or database in a structured format. This data can then be used for a variety of purposes, including data mining, data processing, data cleansing, and data analysis.</p>
        <p>Web scraping tools can be used to extract data from websites and save it to a local file or database in a structured format. This data can then be used for a variety of purposes, including data mining, data processing, data cleansing, and data analysis.</p>
    </body>
    </html>
"""

# 1
"""
soup = BeautifulSoup(html_str, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.p.text)
soup.find('p')
soup.find_all('p')
"""

# 2
"""
import os

html_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), 'index.html')

with open(html_path, 'r') as html_file:
    doc = html_file.read()

soup = BeautifulSoup(doc, 'html.parser')
anchors = soup.find_all('a')
for anchor in anchors:
    print(anchor)
_italics = soup.find_all('b')[-1].find('i').text.strip()
"""

# 3
"""
url = "https://kallyas.github.io/cakeshop/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.contents)
"""

# different ways of accessing elements
# id=""
# class_=""
# string=""
# passing two attributes; fulfils both conditions
# element.parent
# element.children