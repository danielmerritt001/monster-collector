from django.shortcuts import render

# Create your views here.

class Monster:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

monsters = [
  Monster('Lolo', 'eldritch horror', 'Kinda rude.', 3),
  Monster('Sachi', 'werewolf', 'Looks like a turtle.', 0),
  Monster('Fancy', 'cyclops', 'Happy fluff ball.', 4),
  Monster('Bonk', 'witch', 'Meows loudly.', 6)
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def monster_index(request):
  print('hello')
  return render(request, 'monsters/index.html', {'monsters': monsters})
