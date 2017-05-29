from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from myprofile.models import User,UserAvatar
from comments.models import Comment
from myprofile.forms import UserCreationForm,ProfileForm,UserAvatarForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic.base import TemplateView

def main(request):
    commentsList=Comment.objects.all().order_by('-date')[:3]
    return render(request, 'index.html',{'commentsList':commentsList})

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

@csrf_protect
def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    message = 'Ваш профиль был изменен!'
    error = 'Ошибка при заполнении полей'
    profile=()
    try:
        profile=UserAvatar.objects.get(user_id=request.user.id)
    except:
        pass
    form = ProfileForm(instance = request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {'form': form,'profile':profile,'message': message})
        return render(request, 'profile.html', {'form': form,'profile':profile,'error': error})
    return render(request, 'profile.html', {'form': form,'profile':profile,})

@csrf_protect
def imageLoad(request):
    if request.method == 'POST':
        form = UserAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            preavatar=None
            try:
                preavatar=UserAvatar.objects.get(user_id=request.user.id)
            except:
                pass
            if preavatar is not None:
                preavatar.avatar=form.cleaned_data['avatar']
                preavatar.save()
            else:
                response = form.save(commit=False)
                response.user = request.user
                response.save()
            return render(request, 'imageLoad.html', {
                'form': form
                })
    else:
        form = UserAvatarForm(instance = request.user)
    return render(request, 'imageLoad.html', {
        'form': form
    })

class BudgetView(TemplateView):
    template_name = "budget.html"

class LuxView(TemplateView):
    template_name = "lux.html"

class BusinessView(TemplateView):
    template_name = "business.html"
    
class AboutView(TemplateView):
    template_name = "about.html"
