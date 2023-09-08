from django.shortcuts import render
from . import forms


def home_view(request):
    return render(request, 'home/index.html')

def send_message(request):
    form = forms.ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            return render(request, 'home/contact_form.html', {'form': form})
        return render(request, 'home/message_sended.html')
    return render(request, 'home/contact_form.html', {'form': form})
