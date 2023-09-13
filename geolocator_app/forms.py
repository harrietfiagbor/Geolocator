from django import forms
from .models import *


class CoordinateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = '__all__'
