from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def home_page_view(request):
    return render(request, 'testapp/home.html')

def log_out_view(request):
    logout(request)
    return render(request, 'testapp/logout.html')

from testapp.forms import SignupForm
from django.http import HttpResponseRedirect
def signup_view(request):
    form=SignupForm() #get empty form
    if request.method == 'POST':
        form=SignupForm(request.POST) # user details
        user=form.save()
        user.set_password(user.password) #converting to hash password
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request, 'testapp/signup.html', {'form':form})

@login_required
def java_page_view(request):
    return render(request, 'testapp/java_page.html')

@login_required
def python_page_view(request):
    return render(request, 'testapp/python_page.html')

@login_required
def appitude_page_view(request):
    return render(request, 'testapp/appitude_page.html')


