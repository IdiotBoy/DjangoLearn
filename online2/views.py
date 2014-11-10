from django.shortcuts import render_to_response
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            req.session['username'] = username
            return HttpResponseRedirect('/online2/index/')
    else:
        uf = UserForm()
    return render_to_response('online2_login.html', {'uf': uf})

def index(req):
    username = req.session.get('username', '')
    return render_to_response('online2_index.html', {'username':username})

def logout(req):
    del req.session['username']
    return HttpResponse('logout ok!')
    #req.session.