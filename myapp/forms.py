from django import forms
from .models import Data,Account
from django.contrib.auth.models import User

class DataForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    photo = forms.ImageField()
    account_type = forms.ModelChoiceField(queryset=Account.objects.all())
    
    class Meta:
        model = Data
        fields = ['name','email','phone','photo','account_type']



class FilterForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['current_status']
        labels = {'current_status':'category'}

