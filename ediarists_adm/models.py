from django.db import models

# Create your models here.

class Diarist(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=11, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)
    address_number = models.IntegerField(null=False, blank=False)
    neighborhood = models.CharField(max_length=30, null=False, blank=False)
    complement = models.CharField(max_length=100, null=False, blank=True)
    postal_code = models.CharField(max_length=8, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=True)
    state = models.CharField(max_length=2, null=False, blank=False)
    ibge_code = models.IntegerField(null=False, blank=False)
    user_photo = models.ImageField(null=False)
