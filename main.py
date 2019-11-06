import requests
from bs4 import BeautifulSoup

green_result = requests.get("https://jp.indeed.com/jobs?q=python&l=%E6%9D%B1%E4%BA%AC%E9%83%BD")

green_soup = BeautifulSoup(green_result.text, "html.parser")

pagination_info = green_soup.find("div", {"class": "pagination"})

pages = pagination_info.find_all("a")

span = []

for page in pages:
    span.append(page.find("span"));
print(span[0:-1]);