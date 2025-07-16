import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'

requests= requests.get(url)
data = requests.json()

print(f"Name: {data['name']}")
print(f"ID: {data['id']}")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")
print("types:", [t['type']['name'] for t in data['types']])