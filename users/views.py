from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserProfile
from .models import Bloguser


def register(request):
    form = RegisterForm(request.POST)
    user = request.user
    if user.is_anonymous:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('home')
            elif request.method == 'GET':
                form = RegisterForm()
                return render(request, 'users/register.html', {'form': form})

    elif user.is_authenticated:
        messages.info(request, 'You are already registered......vis a vis logged in idiot')
        return redirect('home')

    return render(request, 'users/register.html', {'form': form})


def author(request, id):
    author = Bloguser.objects.get(pk=id)
    post = author.article_set.all()
    return render(request, 'users/author.html', {'author': author, 'post': post})


@login_required
def update_info(request):

    init = request.user
    uname = init.username
    user = Bloguser.objects.get(username=uname)
    url = str(user.profile_pic.url)

    if request.method == 'GET':
        data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile_pic': user.profile_pic,
        }
        form = UserProfile(initial=data)

    elif request.method == 'POST':
        form = UserProfile(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully updated {username}!')
            return redirect('home')
        else:
            print(form.errors)
            username = form.cleaned_data.get('username')
            messages.warning(request, f'Form is not valid {username}!')
            return redirect('profile')
    return render(request, 'users/profile.html', {'form': form, 'user': user, 'url': url})
