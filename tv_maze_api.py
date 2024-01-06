import requests
import json
import pprint

url = 'https://api.tvmaze.com/singlesearch/shows' #?q=girls

params = {"q":"Girls"}

response = requests.get(url,params)

if response.status_code == 200:
    data = json.loads(response.text)
    pprint.pprint(data)
else:
    print(f"ERROR:{response.status_code}")