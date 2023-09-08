from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(label='Imię', required=True)
    email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label="Temat", required=False)
    message = forms.CharField(required=True, label='Wiadomość', widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('name', 'email', "subject", 'message')

    def save(self, commit=True):
        message = Contact.objects.create(
            name=self.cleaned_data.get('name'),
            email=self.cleaned_data.get('email'),
            subject=self.cleaned_data.get('subject'),
            message=self.cleaned_data.get('message')
        )
        if commit:
            message.save()
        return message
