import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
# url = "https://cit-projects-2021.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

# Pass page.content instead of page.text to avoid problems with character encoding
# The .content attribute holds raw bytes, which can be decoded better than the text from the .text attribute.

results = soup.find(id="ResultsContainer")

job_elements = results.find_all('div', class_ = 'card-content')
python_jobs = results.find_all('h2', string=lambda text : 'python' in text.lower())
python_job_elements = [h2_elem.parent.parent.parent for h2_elem in python_jobs]

"""
1. <td>Some Table Data</td>
2. <td></td>
For 1, both .string and .text return what's expected
For 2, .string extracts NoneType and .text extracts an empty string
If the tag has a single string child then the return value is that string.
If the tag has no children or more than one child then the return value is None
If this tag has one child tag then the return value is the 'string' attribute of the child tag, recursively.
.text - gets all the child strings and returns concatenated using the given separator.
"""

# all jobs
# for job_element in job_elements:
#     title_element = job_element.find('h2', class_ = 'title')
#     company_element = job_element.find('h3', class_ = 'company')
#     location_element = job_element.find('p', class_ = 'location')
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print('\n')

# different ways for python jobs

# for i in range(len(python_job_elements)):
#     title_element = python_jobs[i]
#     company_element = python_job_elements[i].find('h3', class_ = 'company')
#     location_element = python_job_elements[i].find('p', class_ = 'location')
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print(f"Apply here: { python_job_elements[i].find_all('a')[1]['href'] }")
#     print('\n')


# for python_job_element in python_job_elements:
#     print(list(list(list(python_job_element.children)[1].children)[3])[1].text.strip())
#     print(list(list(list(python_job_element.children)[1].children)[3])[3].text.strip())
#     print(list(list(list(python_job_element.children)[3].children)[1])[0].text.strip())
#     print(list(list(list(python_job_element.children)[5].children))[3]['href'])
#     print('\n\n')

for python_job_element in python_job_elements:
    title_element = python_job_element.find('h2', class_ = 'title')
    company_element = python_job_element.find('h3', class_ = 'company')
    location_element = python_job_element.find('p', class_ = 'location')
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: { python_job_element.find_all('a')[1]['href'] }")
    print('\n')