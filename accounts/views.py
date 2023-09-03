from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout
from . models import Profile
from django.contrib.auth.models import User
from .forms import UserCreationForm,UserChangeForm

class Register(TemplateView):
    template_name = 'accounts/register.html'

# Create your views here.
def RegistrationView(request):
    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request.user)
    return redirect('register')

def AllUsersView(request):
    if request.user.is_authenticated is None:
        return redirect('login')
    else:
        # user = User.objects.get(pk=request.user.pk)
        profiles = Profile.objects.exclude(user=request.user)
        if request.method == "POST":
            current_user_profile = Profile.objects.get(user=request.user)
            data = request.POST
            action = data.get("follow")
            if action == "follow":
                current_user_profile.follows.add(profile)
            elif action == "unfollow":
                current_user_profile.follows.remove(profile)
            current_user_profile.save()
        return render(request, 'users.html', context={"profiles": profiles})


def AboutUserView(request, pk):
    if request.user.is_authenticated is None:
        return redirect('login')
    else:
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)
        if request.method == "POST":
            current_user_profile = Profile.objects.get(user=request.user)
            data = request.POST
            action = data.get("follow")
            if action == "follow":
                current_user_profile.follows.add(profile)
            elif action == "unfollow":
                current_user_profile.follows.remove(profile)
            current_user_profile.save()
        return render(request, 'about_user.html', context={"profile": profile})


def profile_edit(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()

            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'templates/profile_edit.html', {'form': form})


def MirrorView(request):
    user = Profile.objects.get(user=request.user)
    return render(request, 'mirror.html', context={'user': user})
