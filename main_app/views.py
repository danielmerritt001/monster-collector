from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'Kinda rude.', 3),
  Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def home(request):
  return HttpResponse('<h1>Hello, I am Mike Wazowski</h1>')

def about(request):
  return render(request, 'about.html')

def monster_index(request):
  print('hello')
  return render(request, 'monsters/index.html', {'cats': cats})
