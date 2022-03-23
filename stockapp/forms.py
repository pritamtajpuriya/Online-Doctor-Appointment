from django import forms
from .models import Addpatient
class stockforms(forms.ModelForm):
    class Meta:
        model =Addpatient
        exclude=['seller']

        