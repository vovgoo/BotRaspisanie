
import requests as req
from bs4 import BeautifulSoup

link = "https://vitgtk.belstu.by/raspisanie/"

response = req.get(link).text
soup = BeautifulSoup(response, "lxml")
block = soup.find("iframe").get("src")
print(block)