from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import NotendurForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace with your URL name
        else:
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/login.html')

def index(request):
    if request.method == 'POST':
        form = NotendurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NotendurForm()
    return render(request, 'main/index.html', {'form': form})

def register_view(request):
    return render(request, 'main/register.html')

def contact(request):
    return render(request, 'main/hafa-samband.html')

def form_submit(request):
    if request.method == 'POST':
        form = NotendurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NotendurForm()
    return render(request, 'main/form_submit.html', {'form': form})
