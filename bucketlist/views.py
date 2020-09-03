from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Continent
from .forms import ContactForm, NewPost

from users.models import Bloguser


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


@login_required
def new_post(request):
    init = request.user
    uname = init.username
    user = Bloguser.objects.get(username=uname)

    form = NewPost(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)

            post.author = user
            post.pub_date = timezone.now()
            post.save()

            messages.success(request, f'Post has been published succesfully {user}')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Form')
            return redirect('new_post')

    return render(request, 'bucketlist/new_post.html', {'user': user, 'form': form})
