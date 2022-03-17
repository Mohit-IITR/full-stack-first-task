from django.forms import ModelForm
from .models import Applicants

class ExplorinForm(ModelForm):
    class Meta:
        model = Applicants
        fields = '__all__'