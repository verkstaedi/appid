# dataapp/forms.py
from django import forms
from .models import Notendur

class NotendurForm(forms.ModelForm):
    class Meta:
        model = Notendur
        fields = ['tegund_okutaekis', 'framleidandi', 'gerd', 'nafn', 'simanumer', 'kennitala', 'email', 'lysing']
