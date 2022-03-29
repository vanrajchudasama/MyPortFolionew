from django import forms
from .models import Contact_Us
class ContactForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control','name':'name','placeholder':'Your Name'}))
        email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control','name':'email','placeholder':'Your Email'}))
        name = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'class':'form-control','name':'subject','placeholder':'Subject'}))
        message = forms.CharField(label='Message',widget=forms.TextInput(attrs={'class':'form-control','name':'message','placeholder':'Message'}))

        model=Contact_Us
        fields = '__all__'