from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegistrationForm, CustomUserAuthenticationForm
from .models import CustomUser

def index(request):
    context = {}
    return render(request, 'accounts/index.html', context)


def registration_view(request):
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('accounts:login')
            

        else:
            context = {'form': form}
    
    context = {'form': form}
    
    return render(request, 'accounts/registration.html', context)

def login_view(request):
    form = CustomUserAuthenticationForm()
    
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # if user is not authenticated, it will raise validerror message which is defined in form.py 
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            else:
                return redirect('accounts:login')
                
            
            
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    
    # Better not showing if user is not authenticated, this is a just example code. I can change later.
    if request.user.is_authenticated:
        logout(request)
        return redirect('accounts:login')
    # else:
    #     print('Your are not logged in yet.')
    
    return redirect('accounts:home')