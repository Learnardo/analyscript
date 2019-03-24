
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def analyse(request):
    inputtext = request.GET['inputtext']
    return render(request,'analysis-report.html', {'inputtext':inputtext})
