from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'generator/index.html')

def about(request):
    return render(request, 'generator/about.html')

def links(request):
    return render(request, 'generator/links.html')

