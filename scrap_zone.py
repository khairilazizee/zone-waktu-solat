import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.e-solat.gov.my")
soup = BeautifulSoup(page.content, "parser.html")
# dropdown zone
results = soup.find(id="inputzone")
zones = results.find("option", class_="hs")
res_dict = {}
for zone in zones:
  # zone["value"]
  for value in zone.stripped_strings:
    res_dict[zone["value"]] = value
             
# to convert to json
print(json.dumps(res_dict, indent=4)
