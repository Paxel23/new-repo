from django import forms
from .models import Blockchain,Token

my_default_errors = {
    'required': 'To pole jest wymagane',
    'max_length': 'Wpisana wartość jest za długa'
}

class BlockchainForm(forms.ModelForm):
    class Meta:
        model = Blockchain
        fields = ['name', 'description']
        error_messages = {
            'name': my_default_errors,
            'description': my_default_errors,
           
        }

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['name', 'shortcut','blockchain','description']
        error_messages = {
            'neme': my_default_errors,
            'shortcut': my_default_errors,
            'blockchain': my_default_errors,
            'description': my_default_errors,
           
        }