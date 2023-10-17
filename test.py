import requests
import json


print(type(json.dumps({"1": "2"})))
print(requests.post("http://127.0.0.1:5000/text", json={"text": "adbcd"}).text)