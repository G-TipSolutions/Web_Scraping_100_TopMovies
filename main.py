import requests
from bs4 import BeautifulSoup

# Insert what ever website below // make sure to check for 
# website.com/robot.txt in browser to see what will be blocked
# from scraping

URL = "https://web.sitewithMoviesxxxEXAMPLE.com"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]

#  reorder the list with short function
movies = movie_titles[::-1]

with open(file="movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

