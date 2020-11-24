from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm

from .models import Article


class ContactForm(forms.Form):
    username = forms.CharField(label="Your Name", max_length=120)
    email = forms.EmailField(label="Your Email Address", max_length=150)
    subject = forms.CharField(label="Subject")
    message = forms.CharField(label="Write your heart out", widget=forms.Textarea)

    def contactMail(self):
        subject = self.cleaned_data['form.subject'] + " from " + self.cleaned_data['form.sender']
        message = self.cleaned_data['form.message']
        sender = settings.EMAIL_HOST_USER
        recipients = ['hari.kannan@outlook.com']

        send_mail(subject, message, sender, recipients, fail_silently='false')


class NewPost(ModelForm):

    class Meta:
        model = Article
        fields = ['c_name', 'title', 'content']


class UpdatePost(ModelForm):

    class Meta:
        model = Article
        fields = ['c_name', 'title', 'content']
