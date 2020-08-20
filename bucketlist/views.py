from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Countries
from .forms import ContactForm


# Create your views here.
def home(request):
    name_list = Countries.objects.all()
    context = {'name_list': name_list}
    return render(request, 'bucketlist/home.html', context)


def contact_us(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.contactMail()
            messages.success(request, 'Thank you for your kind thoughts')
            return redirect('home')

        else:

            form = ContactForm()

    return render(request, 'bucketlist/contact_us.html', {'form': form})


def country_blog(request, country):
    name = Countries.objects.get(country_name=country)
    blogpost = name.countrypage_set.all()
    return render(request, 'bucketlist/country_page.html', {'blogpost': blogpost, 'name': name})


def article_page(request, country, id):
    name = Countries.objects.get(country_name=country)
    if name:
        blogpost = name.countrypage_set.get(pk=id)
        return render(request, 'bucketlist/article_page.html', {'blogpost': blogpost, 'name': name})
    else:
        return render(request, 'bucketlist/', {'name': name})
