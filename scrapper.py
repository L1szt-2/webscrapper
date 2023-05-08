import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#finding elements by ID 

results = soup.find(id="ResultsContainer")

# print(results.prettify())

#find elements by class name 

job_elements = results.find_all("div", class_="card-content")

# loops through jobs for title, company name, location

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# finding python jobs 
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

print(len(python_jobs))             #prints num of jobs containing python

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
