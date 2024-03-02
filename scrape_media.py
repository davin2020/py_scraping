
#  NEW FILE 
# Use an HTML Parser for Web Scraping in Python
# $ python -m pip install beautifulsoup4

# beauty_soup.py - need torun - pup  install requests
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://www.thetappingsolution.com/2024event/R00Ms/D5-MED.php"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# "html.parser" represents Python’s built-in HTML parser.

# , BeautifulSoup objects have a .get_text() method that you can use to 
# extract all the text from the document and automatically remove any HTML tags.

print("got page")
# print(soup.get_text())

audio_files = soup.find("audio")
# print(len(audio_files))
# thefile = audio_files.text.strip()  # thsi doesnt actually work
# print("thefile ", thefile)
print("audio source ", audio_files["src"]) # this does work 

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

# try to save locally, old file will get overwritten
u = audio_files["src"]
with open(u.split("/")[-1], "wb") as f_out:
        f_out.write(requests.get(u, headers=headers).content)