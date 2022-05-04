from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.
def home(request):
    return HttpResponse('home')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')