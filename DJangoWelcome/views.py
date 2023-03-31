from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def homepage(request):
    return render(request, "welcome.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Website Inquiry'
            body = {
                'antwoord1': form.cleaned_data['antwoord1'],
                'antwoord2': form.cleaned_data['antwoord2'],
                'antwoord3': form.cleaned_data['antwoord3'],
                'antwoord4': form.cleaned_data['antwoord4'],
                'antwoord5': form.cleaned_data['antwoord5'],
                'antwoord6': form.cleaned_data['antwoord6'],
                'antwoord7': form.cleaned_data['antwoord7'],
            }
            message = "\n".join(body.values())

            form = ContactForm()
            return render(request, "welcome.html", {'form':form})