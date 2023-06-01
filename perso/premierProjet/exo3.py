import requests
from bs4 import BeautifulSoup
import json

allPorts = {}
i = 1
while i < 10:
    req = requests.get(f"https://www.frameip.com/liste-des-ports-tcp-udp/?plage={i}")
    soup = BeautifulSoup(req.content, 'html.parser').find("table")
    soupRows = soup.find_all('tr')

    for soupRow in soupRows[1:]:
        port = soupRow.find("a").string
        protocol = soupRow.find_all("a")[1].string
        name = soupRow.find("p").string.strip()
        desc = soupRow.find_all("p")[3].string.strip()
        allPorts[port] = {}
        allPorts[port][protocol] = {}
        allPorts[port][protocol][name] = desc
    i += 1

with open("ports.json", "w") as json_file_pointer:
  json.dump(allPorts, json_file_pointer, indent=4)

print(allPorts)