import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = '802fc5c651ee0bc38f034cba6dcbab40'
header = {'Content-Type':'application/json', 'trainer_token': token}
trainer_id = '27915'

def test_homework():
    
    response = requests.get(url = f'{url}/trainers', headers = header)
    assert response.status_code == 200

def test_homework_2():
    
    response = requests.get(url = f'{url}/trainers?trainer_id=27915', headers = header)
    assert response.json()['data'][0]['trainer_name'] == 'Редли Флейм'




