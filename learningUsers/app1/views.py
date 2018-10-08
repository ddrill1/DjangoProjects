from django.shortcuts import render
from app1.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in, NICE!')

@login_required
def userLogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileInfoForm(data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']

            profile.save()

            registered = True
        else:
            print(userForm.errors,profileForm.errors)
    else:
        userForm = UserForm()
        profileForm = UserProfileInfoForm()

    return render(request,'app1/registration.html',
                {'userForm':userForm,
                'profileForm':profileForm,
                'registered':registered})

def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE!')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and password: {}'.format(username,password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request, 'app1/login.html', {})
