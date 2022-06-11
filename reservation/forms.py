from pyexpat import model
from django import forms
from .models import reservation


class ReserveForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields = '__all__'

