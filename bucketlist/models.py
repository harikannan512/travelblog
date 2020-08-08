from django.db import models
from django import forms
from django.core.mail import send_mail


class Countries(models.Model):
    country_name = models.CharField(max_length=20)
    description = models.TextField()
    img_url = models.CharField(max_length=30, default='static/default.jpg')

    def __str__(self):
        return self.country_name

    def pic_url(self):
        return self.img_url


class ContactForm(forms.Form):
    username = forms.CharField(label="Your Name", max_length=20)
    email = forms.EmailField(label="Your Email Address", max_length=50)
    subject = forms.CharField(label="Subject")
    message = forms.CharField(label="Write your heart out", widget=forms.Textarea)

    def contactMail(self):
        if self.is_valid():
            subject = self.cleaned_data['self.subject']
            message = self.cleaned_data['self.message']
            sender = self.cleaned_data['self.email']

            recipients = ['harikannan512@gmail.com']
            send_mail(subject, message, sender, recipients)
