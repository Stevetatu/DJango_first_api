from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lesson(request):
    return HttpResponse('<h1>My teachers page</h1>')