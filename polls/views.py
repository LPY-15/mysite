from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "polls/index.html")

def details(request):
    return render(request, 'polls/detail.html')

def results(request):
    return render(request, 'polls/results.html')