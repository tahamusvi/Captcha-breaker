from django import forms
from .models import captcha

class CaptchaForm(forms.ModelForm):
    class Meta:
        model = captcha
        fields = '__all__'  
        exclude = ['answered', 'image'] 
        # labels = {'field1': 'Custom Label'}  
        # widgets = {'field1': forms.TextInput(attrs={'class': 'custom-class'})} 