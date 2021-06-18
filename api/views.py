from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.diarists_by_city import list_diarists_by_city
from .serializer import serializer_diarists_by_city
from .pagination.diarists_by_city import DiaristsByCityPagination

# Create your views here.

class DiaristsCityList(APIView, DiaristsByCityPagination):
    def get(self, request, format=None):
        postal_code = self.request.query_params.get('postal_code', None)
        diarists = list_diarists_by_city(postal_code)

        result = self.paginate_queryset(diarists, request)

        serializer = serializer_diarists_by_city.SerializerDiaristsByCity(
            result, 
            many=True,
            context={'request': request}
        )

        return self.get_paginated_response(serializer.data)