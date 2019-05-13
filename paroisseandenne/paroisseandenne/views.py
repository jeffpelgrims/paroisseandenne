from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def home_page(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        mail_from = request.POST['nom_complet'], request.POST['email']
        mail_to = [settings.EMAIL_HOST_USER]

        send_mail(
            'Site paroisse Andenne',
            message,
            mail_from,
            mail_to,
            fail_silently=False,
        )

    form = ContactForm(request.POST or None, auto_id=False)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)