from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=60, verbose_name="Imię")
    email = models.EmailField(max_length=100, verbose_name="Email")
    message = models.TextField(verbose_name="Wiadomość")
    subject = models.CharField(max_length=100, verbose_name="Temat")

    def __str__(self):
        return self.name + ': ' + self.subject