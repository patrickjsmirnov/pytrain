
import requests

group_id = '-22746750'
url = 'https://api.vk.com/method/wall.get'
token = 'generate_your_token'

r = requests.get(url, params={
    'owner_id': group_id,
    'count': 100,
    'offset': 0,
    'access_token': token,
    'v': 5.52
})

print(r.json())