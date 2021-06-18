import requests

def search_city_postal_code(postal_code):
    response = requests.get(f'https://viacep.com.br/ws/{postal_code}/json/')

    return response