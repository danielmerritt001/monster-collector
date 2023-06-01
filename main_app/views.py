from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster, Bane
from .forms import ChecklistForm

# classes
class MonsterCreate(CreateView):
  model = Monster
  fields = ['name', 'breed', 'description', 'age']

class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['breed', 'description', 'age']

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/'

class BaneCreate(CreateView):
  model = Bane
  fields = '__all__'

class BaneList(ListView):
  model = Bane

class BaneDetail(DetailView):
  model= Bane

class BaneUpdate(UpdateView):
  model = Bane
  fields = ['name', 'color']

class BaneDelete(DeleteView):
  model = Bane
  success_url = '/banes/'

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
  banes_monster_doesnt_have = Bane.objects.exclude(id__in = monster.toys.all().values_list('id'))
  checklist_form=ChecklistForm()
  return render(request, 'monsters/detail.html', { 'monster': monster, 'checklist_form': checklist_form, 'banes': banes_monster_doesnt_have})

def add_checklist(request, monster_id):
  form = ChecklistForm(request.POST)
  if form.is_valid():
    new_checklist = form.save(commit=False)
    new_checklist.monster_id = monster_id
    new_checklist.save()
  return redirect('monster-detail', monster_id=monster_id)