from django.shortcuts import render
from .models import Countries


# Create your views here.
def home(request):
    name_list = Countries.objects.all()
    context = {'name_list': name_list}
    return render(request, 'bucketlist/home.html', context)
