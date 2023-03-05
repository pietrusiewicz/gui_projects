import requests as r
import json

jsonfile = json.loads(r.get("https://danepubliczne.imgw.pl/api/data/synop").content)

for line in jsonfile:
    print(line['stacja'])

