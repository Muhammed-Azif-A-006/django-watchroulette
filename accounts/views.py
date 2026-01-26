from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from  .models import Profile
from .forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def hello(request):
    if request.method == "GET":
        return render(request,"accounts/hello.html",{"name" :"Muhammed Azif"})

@login_required
def profiles(request):
    allprof = Profile.objects.all()
    return render(request,"accounts/profiles.html",{'profiles':  allprof })
@login_required
def add_profile(request):
    if request.method ==  'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    else:
        form = ProfileForm()
    return render(request,"accounts/add_profile.html",{"form" : form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # return to the page user originally wanted (if provided)
            next_url = request.POST.get("next") or request.GET.get("next")
            if next_url:
                return redirect(next_url)

            # default landing page after login
            return redirect(getattr(settings, "LOGIN_REDIRECT_URL", "/watch/"))

        return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")

def logout_view(request):
	logout(request)
	return redirect("login")
