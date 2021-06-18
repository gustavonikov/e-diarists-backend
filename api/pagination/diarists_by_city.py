from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DiaristsByCityPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        remaining_diarists = (self.page.paginator.count - self.page_size) if self.page.paginator.count > self.page_size else 0

        return Response({
            'remaining_diarists': remaining_diarists,
            'diarists': data
        })