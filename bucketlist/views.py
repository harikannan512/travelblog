from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Continent
from .forms import ContactForm


# Create your views here.
def home(request):
    name_list = Continent.objects.all()
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


def continent_blog(request, id):
    name = Continent.objects.get(pk=id)
    blogpost = name.article_set.all()
    return render(request, 'bucketlist/continent_page.html', {'blogpost': blogpost, 'name': name})


def article_page(request, id, pid):
    name = Continent.objects.get(pk=id)
    if name:
        post = name.article_set.get(pk=pid)
        return render(request, 'bucketlist/article_page.html', {'post': post, 'name': name})
    else:
        return render(request, 'bucketlist/', {'name': name})
