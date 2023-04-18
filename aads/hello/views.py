from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.\n<a href='/mkmoney'>Make Money</a>")

def mkmoney(request):
	return render(request, "mkmoney.html")
