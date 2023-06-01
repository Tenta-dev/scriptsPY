import requests
from bs4 import BeautifulSoup
import re

req = requests.get("https://www.frameip.com/liste-des-ports-tcp-udp/?plage=1")
tabl = BeautifulSoup(req.content, 'html.parser')
# title = soup.find("h1")
for aa in tabl.find_all('tr'):
    ff = aa.find("td")
    gg = ff.find("p").string
    print(gg)
    break