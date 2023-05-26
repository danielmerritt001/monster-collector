from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello, I am Mike Wazowski</h1>')

def about(request):
  return render(request, 'about.html')
