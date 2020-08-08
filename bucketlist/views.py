from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Countries, ContactForm


# Create your views here.
def home(request):
    name_list = Countries.objects.all()
    context = {'name_list': name_list}
    return render(request, 'bucketlist/home.html', context)


def contact_us(request):
    form = ContactForm(request.POST)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            context['form'].contactMail()
            messages.add_message(request, messages.SUCCESS, 'Thank you for your messages.')
            return HttpResponseRedirect(request, 'bucketlist/contact_us.html', context)
        else:
            form = ContactForm()
    return render(request, 'bucketlist/contact_us.html', context)
