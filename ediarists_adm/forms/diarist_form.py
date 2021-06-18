import json

from ediarists_adm.services.postal_code import search_city_postal_code
from django import forms
from ..models import Diarist

class DiaristForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))
    
    class Meta:
        model = Diarist
        exclude = ('ibge_code',)

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']

        return cpf.replace('.', '').replace('-', '')

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']

        formatted_postal_code = postal_code.replace('-', '')
        response = search_city_postal_code(formatted_postal_code)

        if response.status_code == 400:
            raise forms.ValidationError('O CEP informado está incorreto.')

        api_city = json.loads(response.content)

        if 'erro' in api_city:
            raise forms.ValidationError('O CEP informado não foi encontrado!')

        return formatted_postal_code

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        return phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

    def save(self, commit=True):
        instance = super(DiaristForm, self).save(commit=False)
        response = search_city_postal_code(self.cleaned_data.get('postal_code'))
        api_city = json.loads(response.content)
        instance.ibge_code = api_city['ibge']
        instance.save()

        return instance