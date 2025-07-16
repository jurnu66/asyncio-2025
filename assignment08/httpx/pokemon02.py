import requests
import time

pokemon_name = ['pikachu', 'charmander', 'bulbasaur', 'squirtle', 'snorlax']
start = time.time()
for name in pokemon_name:
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    data = response.json()
    
    print(f"{data['name'].title()} (id: {data['id']}) types: {', '.join([t['type']['name'] for t in data['types']])}")