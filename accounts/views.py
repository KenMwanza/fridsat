from accounts.decorators import anonymous_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

@anonymous_required(home_url='/')
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')


