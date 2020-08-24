from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserProfile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def update_info(request):
    user = request.user
    if request.method == 'GET':
        data = {
            'username': 'user.username',
            'email': 'user.email',
            'first_name': 'user.first_name',
            'last_name': 'user.last_name'
        }
        form = UserProfile(initial=data)
    elif request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully updated {username}!')
            return redirect('home')
    return render(request, 'users/profile.html', {'form': form, 'user': user})
