from django.shortcuts import render, render_to_response
from django.template import loader, Context, Template
from django.http import HttpResponse
from blog.models import Employee, Entry, Blog

# Create your views here.
def index(req):
    t = loader.get_template('index.html')
    c = Context({'uname': 'alen'})
    return HttpResponse(t.render(c))

def index1(req):
    t = Template('<h1>hello {{uname}}</h1>')
    c = Context({'uname': 'terry'})
    return HttpResponse(t.render(c))
    
def index2(req):
    return render_to_response('index.html', {'uname': 'terry xu'})

def model(req):
    emp = Employee()
    emp.name = 'Alen'
    emp.save()
    return HttpResponse('ok')
    
def model2(req):
    emp = Employee(name='terry')
    emp.save()
    return HttpResponse('ok')

def model3(req):
    Employee.objects.create(name='Max')
    return HttpResponse('ok')

def modelAll(req):
    emps = Employee.objects.all()
    return render_to_response('index.html', {'emps':emps})

def bloginit(req):
    entry1 = Entry.objects.create(name='alen')
    entry2 = Entry.objects.create(name='max')
    entry3 = Entry.objects.create(name='carl')
    blog1 = Blog.objects.create(name='alen_blog1', entry=entry1)
    return HttpResponse('ok')