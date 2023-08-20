from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from blog.models import Post


# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.  You are now logged in!')

            #login with created account
            new_user = auth.authenticate(username=username, password=form.cleaned_data['password1'],)
            auth.login(request, new_user)
            return HttpResponseRedirect('/profile')
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return HttpResponseRedirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        post = Post.objects.filter(author=request.user).count()

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'post' : post,
    }
    return render(request, 'accounts/profile.html', context)