import requests
from bs4 import BeautifulSoup

# Take input (year)
nostalgic_date = input("On which date you wanna see billboard hot 100 songs?(YYYY-MM-DD): ")
URL = "https://www.billboard.com/charts/hot-100/{}".format(nostalgic_date)

# Getting website HTML
response = requests.get(URL)
website_html = response.text

# Beautiful Soup Web Scraping
soup = BeautifulSoup(website_html, "html.parser")
web_scrap = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
trash_list = ["Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:", "Additional Awards",
              "Gains in Weekly Performance", "Have a Tip?", "Follow Us", "The Daily"]

# Organize the data received into a list
song_titles = [title.text.strip()
               for title in web_scrap if title.text.strip() not in trash_list]

# Print the songs
for count, song in enumerate(song_titles, 1):
    if not count > 100:
        print("{}: {}".format(count, song))
