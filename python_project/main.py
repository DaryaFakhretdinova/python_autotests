import requests
import time


url = 'https://api.pokemonbattle.ru/v2'
token = '802fc5c651ee0bc38f034cba6dcbab40'
header = {'Content-Type':'application/json', 'trainer_token': token}
trainer_id = '27915'

# 1 Создаём покемона

body = {
    "name": "Пикапика",
    "photo_id": -1
}

response = requests.post(url = f'{url}/pokemons', headers = header, json = body)
time.sleep(1)
print(response)

# записываем айди

pokemon_id = response.json()['id'] 

# 2 Меняем имя покемону
body_name = {
    "pokemon_id": f'{pokemon_id}',
    "name": "generate",
}

response = requests.patch(url = f'{url}/pokemons', headers= header, json = body_name) 
time.sleep(1)
print(response)

# 3 Ловим покемона в покебол

body_catch = {

    "pokemon_id": f'{pokemon_id}'
}

response = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_catch)
print(response)
print('Успех')
