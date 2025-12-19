import requests
from bs4 import BeautifulSoup
print("hello")

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response=requests.get(URL)
empire_website=response.text

soup=BeautifulSoup(empire_website,'html.parser')

titles=[i.getText() for i in soup.find_all(name='h3',class_="title")]
titles=titles[::-1]

print("adding movies list into the movies.txt file...")

with open("Day 45/100 movies to watch start/Movies.txt", 'a', encoding='utf-8') as file:
    for i in titles:
        file.write(i + "\n")
print("Movies..txt file created...")

