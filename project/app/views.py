from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:
        return render(request, 'index.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('home')
            else:
                messages.warning(request, 'Registration saved but unable to log you in automatically. Please log in.')
                return redirect('home')
        else:
            # Form invalid -> re-render with errors
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in to view that record.")
        return redirect('home')

def delete_record(request, pk):
        if request.user.is_authenticated:
            delete_record = Record.objects.get(id=pk)
            delete_record.delete()
            messages.success(request, "Record deleted successfully.")
            return redirect('home')
        else:
            messages.error(request, "You must be logged in to view that record.")
            return redirect('home')
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('home')