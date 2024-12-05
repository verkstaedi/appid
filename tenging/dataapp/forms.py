# dataapp/forms.py
from django import forms
from .models import Notendur

class NotendurForm(forms.ModelForm):
    class Meta:
        model = Notendur
        fields = ['nafn', 'bilnumer', 'vandamal', 'stadsetning', 'buid_til', 'kennitala', 'simanumer']
