from django import forms
from django.forms import ModelForm
from . models import applicants

class NameForm(ModelForm):
    class Meta:
        model = applicants
        fields = '__all__'