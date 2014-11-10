from django.shortcuts import render, render_to_response
from django import forms  
from django.http.response import HttpResponse, HttpResponseRedirect
from online.models import User
from pip._vendor.requests.models import Response

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def register(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #print username, password
            User.objects.create(username = username, password = password)
            return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('online_register.html', {'uf': uf})

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            users = User.objects.filter(username__exact = username, password__exact = password)
            if users:
                response = HttpResponseRedirect('/online/index/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf})

def index(req):
    username = req.COOKIES.get('username', '')
    print username
    return render_to_response('online_index.html', {'username': username})

def logout(req):
    res = HttpResponse()
    res.delete_cookie('username')
    return res
    