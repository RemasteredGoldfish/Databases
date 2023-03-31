from django import forms 
class ContactForm(forms.Form):
    antwoord1 = forms.CharField(max_length = 30)
    antwoord2 = forms.CharField(max_length = 30)
    antwoord3 = forms.CharField(max_length = 30)
    antwoord4 = forms.CharField(max_length = 30)
    antwoord5 = forms.CharField(max_length = 30)
    antwoord6 = forms.CharField(max_length = 30)
    antwoord7 = forms.CharField(max_length = 30)
