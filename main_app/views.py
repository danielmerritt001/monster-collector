from django.shortcuts import render
from .models import Monster

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def monster_index(request):
  monsters = Monster.objects.all()
  return render(request, 'monsters/index.html', {'monsters': monsters})

def monster_detail(request, monster_id):
  monster = Monster.objects.get(id=monster_id)
  return render(request, 'monsters/detail.html', { 'monster': monster})