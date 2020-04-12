from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#def index(request):
#    return HttpResponse("This is index")


def index(request):
    return render(request, 'index/index.html')


def analyse(request):

    return render(request, 'index/index.html')
