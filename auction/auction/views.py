from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
# csrf_token = ''
@login_required
def profile_view(request):
    context = {}
    return render(request, 'profile.html', context)



def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance = request.user)
        
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('home-view')
            
    else:
        form = EditProfileForm(instance = request.user)
        context = {'form': form}   
        return render(request, 'edit_profile.html', context)


def reg_view(request):
    form = RegisterForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('DATA RECEIVED')
        print(form.errors)
        
        if form.is_valid():
            print('DATA IS VALID')
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('home-view')
    return render(request, 'register.html', context)
    

@login_required
def home_view(request):
    context = {'username': None}
    return render(request, 'home.html', context)




def login_view(request):
    error_message = None
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            
            # csrf_token = django.middleware.csrf.get_token(request)
            
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('http://127.0.0.1:5173/')
        else:
            error_message = 'Incorrect Password and/or Username.'
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

###########################################################

@login_required
def logout_view(request):
    print('logout requested')
    logout(request)
    return redirect('home-view')

