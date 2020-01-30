import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://jp.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination_info = soup.find("div", {"class": "pagination"})

    links = pagination_info.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    
    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        print(result.find("div", {"class": "title"}).string)
    return jobs