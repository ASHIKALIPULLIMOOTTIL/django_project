from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def print_hello(request):
    movie_det={'movies':[
        {'title':'it1',
        'year': 2008,
        'summary':'sacry',
        'sucess': True},
        {'title':'it2',
        'year': 2012,
        'summary':'sacry',
        'sucess': False},
        {'title':'it3',
        'year': 2020,
        'summary':'sacry',
        'sucess': False},
    ]
    }
    return render(request,'hello.html',movie_det)