from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass
