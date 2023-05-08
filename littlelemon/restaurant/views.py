from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse('hello world')


def index(request):
    return render(request, 'index.html', {})
