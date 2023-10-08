import requests as rq
url = 'https://realpython.github.io/fake-jobs/'
page = rq.get(url)
#print(page.text)

# Use beautifulsoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)


# Find element from my page by ID
results = soup.find(id='ResultsContainer')
#print(results.prettify())

# Find elements by HTML class name
job_elements = results.find_all('div', class_='card-content')

for je in job_elements:
    print(je, end="\n"*2)

# Filter down further

''' for je in job_elements:
    title_element = je.find('h2', class_='title')
    company_element = je.find('h3', class_='company')
    location_element = je.find('p', class_='location')
    print(title_element)
    print(company_element)
    print(location_element)
    print()

# Adapted to get the text
print('Printing the text from the elements')
print('-'*80)
for je in job_elements:
    title_element = je.find('h2', class_='title')
    company_element = je.find('h3', class_='company')
    location_element = je.find('p', class_='location')
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()

# Adapted to get the text stripped
print('Printing the text from the elements with strip')
print('-'*80)
role_type = []
company = []
for je in job_elements:
    title_element = je.find('h2', class_='title')
    company_element = je.find('h3', class_='company')
    location_element = je.find('p', class_='location')
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    role_type.append(title_element.text.strip())
    company.append(company_element.text.split()) 
    print()

print(role_type)
print(company)
# Create a data frame
import pandas as pd
df = pd.DataFrame({'role': role_type,
              'company': company})

print(df)

#Find elements by Class Name and Text Content
python_jobs = results.find_all('h2', string='Python')
print(python_jobs)

# Pass a function to a beautiful soup method
python_jobs = results.find_all(
    'h2', string=lambda text: 'python' in text.lower()
)
print(len(python_jobs))
print(python_jobs)

# Access child objects
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Find the hyperlinks with the anchor tag
for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n") '''


# Try it on my website
url = 'https://hutsons-hacks.info/'
page = rq.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='content')
blog_elements = results.find_all('div', class_='site-content')
print(blog_elements)