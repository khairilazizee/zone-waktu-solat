import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.e-solat.gov.my")
soup = BeautifulSoup(page.content, "html.parser")
# search for dropdown zone
results = soup.find(id="inputzone")
# print(results.prettify())
zones = results.find_all("option", class_="hs")
res_dict = {}
for zone in zones:
    for value in zone.stripped_strings:
        res_dict[zone["value"]] = value

# convert to json
print(json.dumps(res_dict, indent=4))
