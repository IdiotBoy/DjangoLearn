# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from model_form.models import Author, Book, AuthorForm, BookForm

def author(req):
	if (req.method == 'POST'):
		form = AuthorForm(req.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('OK')
	else:
		form = AuthorForm()
	return render_to_response('index2.html', {'form': form})

def book(req):
	if (req.method == 'POST'):
		form = BookForm(req.POST)
		if form.is_valid():
			return HttpResponse('OK')
		else:
			print form['name']
			print form['name'].errors
			print form['name'].errors.as_json()
			print form.errors
			print ''
	else:
		form = BookForm()

	return render_to_response('index2.html', {'form': form})

def view_author(req):
	id = req.GET.get('id')
	author = Author.objects.get(id==id)
	form = AuthorForm(instance=author)
	return render_to_response('index2.html', {'form': form})

def view_book(req):
	id = req.GET.get('id')
	book = Book.objects.get(id==id)
	form = BookForm(instance=book)
	return render_to_response('index2.html', {'form': form})
