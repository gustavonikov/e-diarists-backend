import json
from ediarists_adm.services.postal_code import search_city_postal_code
from ediarists_adm.models import Diarist
from rest_framework import serializers

def list_diarists_by_city(postal_code):
    ibge_code = search_city(postal_code)['ibge']

    try:
        diarists = Diarist.objects.filter(ibge_code=ibge_code).order_by('id')

        return diarists
    except Diarist.DoesNotExist:
        return []

def search_city(postal_code):
    response = search_city_postal_code(postal_code)

    if response.status_code == 400:
        raise serializers.ValidationError('O CEP informado está incorreto.')

    api_city = json.loads(response.content)

    if 'erro' in api_city:
        raise serializers.ValidationError('O CEP informado não foi encontrado!')

    return api_city
