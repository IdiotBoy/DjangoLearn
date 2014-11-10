from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.
def init(req):
    User.objects.create_user('john', 'xx@xx', '123456')
    return HttpResponse('ok')
    
def index(req):
    print 'req.user', req.user
    if not req.user.is_authenticated():
        return HttpResponse('no anthenticated')
    else:
        return HttpResponse('anthenticated, %d, %s' % (req.user.id, req.user.username))

def login_v(req):
    username = 'john'
    pw = '123456'
    user = authenticate(username=username, password=pw)
    if user is not None:
        login(req, user)
        return HttpResponse(user.username)
    else:
        return HttpResponse('fail')

def logout_v(req):
    logout(req)
    return HttpResponse('logout')