from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from myprofile.models import User
from myprofile.forms import UserCreationForm

def main(request):
    return render(request, 'index.html')

@csrf_protect
def login(request):
    args = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = 'Email или пароль введены неверно'
            return render(request, 'login.html',{'error':error})

    return render(request, 'login.html', args)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_protect
def registrate(request):
    args={}
    args['form']=UserCreationForm()
    if request.POST:
        newuser_form=UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                email=newuser_form.cleaned_data['email'],
                password=newuser_form.cleaned_data['password2']
                )
            auth.login(request,newuser)
            return HttpResponseRedirect('/')
        else:
            args['form']=newuser_form
    return render(request,'registrate.html', args)
