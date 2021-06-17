from django import forms
from ..models import Diarist

class DiaristForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))

    class Meta:
        model = Diarist
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']

        return cpf.replace('.', '').replace('-', '')

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']

        return postal_code.replace('-', '')

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        return phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')