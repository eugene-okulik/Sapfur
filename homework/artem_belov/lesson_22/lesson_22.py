import requests
from datetime import datetime


start = datetime.now()
response = requests.get('https://api.restful-api.dev/objects')
print(response)
end = datetime.now()
print(end - start)