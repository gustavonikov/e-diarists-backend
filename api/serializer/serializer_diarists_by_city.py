from rest_framework import serializers
from ediarists_adm.models import Diarist
import random

class SerializerDiaristsByCity(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Diarist
        fields = ('full_name', 'user_photo', 'city', 'rating')

    def get_rating(self, obj):
        random.randint(0, 5)