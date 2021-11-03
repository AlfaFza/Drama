from django import forms

from .models import shop


class ModelForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','img','rating']