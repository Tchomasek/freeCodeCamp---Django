from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args,**kkwargs):
    return render(request, 'home.html', {})

def contacts(*args,**kkwargs):
    return HttpResponse('<h1>contacts</h2>')
