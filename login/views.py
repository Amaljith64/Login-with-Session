from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control



# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'username' in request.session:
        return redirect(home)
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # login(request,user)
            request.session['username'] = username
            return redirect(home)
        else:
            messages.error(request, '*Invalid Username or Password')
            return redirect(login)

    return render(request, 'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')

    return redirect(login)


def logout (request):
    if 'username' in request.session:
        request.session.flush()
    # auth.logout(request)
    return redirect(login)

    # return render(request,'login.html')
