from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args,**kkwargs):
    return render(request, 'home.html', {})

def about_view(request, *args,**kkwargs):
    my_context = {
        'title': 'this is about us',
        "this_is_true": True,
        'my_number': 123,
        'my_list': [123,456,321,'abc'],
        'my_html': "<h2>Hello world</h1>"
    }
    return render(request, 'about.html', my_context)

def contact_view(request, *args,**kkwargs):
    return render(request, 'contact.html', {})

def social_view(request, *args,**kkwargs):
    return HttpResponse('<h1>Social Page</h1>')
