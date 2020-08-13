from django.shortcuts import render
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
            message = "Thank you for your messages."
            return render(request, '/bucketlist/', {'form': form, 'message': message})

        else:

            form = ContactForm()

    return render(request, 'bucketlist/contact_us.html', {'form': form})


def country_blog(request, id):
    name = Countries.objects.get(pk=id)
    blogpost = name.countrypage_set.all()
    return render(request, 'bucketlist/country_page.html', {'blogpost': blogpost, 'name': name})
