from django.contrib.auth import authenticate, login, logout
from gamesystem.form import createUserForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "pages/home.html")


def registersystem(request):
    form = createUserForm()
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid:
            form.save
            messages.success(request, "Account created for")
        return redirect('login')
    context = {'form': form}
    return render(request, "pages/register.html", context)


def loginsystem(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or Password is incorrect')

    context = {}
    return render(request, "pages/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')
