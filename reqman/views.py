from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the home page of the app. This is where the entry form will be.")
