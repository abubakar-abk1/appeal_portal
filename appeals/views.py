from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppealForm
from .models import Post

def submit_appeal(request):
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AppealForm()

    return render(request, 'submit.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    posts = Post.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})


def main(request):
    return render(request, 'main.html')

def signup(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=firstname,
                    last_name=lastname
                )
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')

def page(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'page.html', {'pk' : pk})

