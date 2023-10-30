import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
r = requests.get(url).content
soup = BeautifulSoup(r, 'html.parser')

# Find the list of book titles
titles = soup.find_all("h3")
for i, title in enumerate(titles, 1):
    print(f"Book {i}: {title.a['title']}")
