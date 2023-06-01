from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster
from .forms import ChecklistForm

# classes
class MonsterCreate(CreateView):
  model = Monster
  fields='__all__'

class MonsterUpdate(UpdateView):
  model = Monster
  fields = ['breed', 'description', 'age']

class MonsterDelete(DeleteView):
  model = Monster
  success_url = '/monsters/'

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
  checklist_form=ChecklistForm()
  return render(request, 'monsters/detail.html', { 'monster': monster, 'checklist_form': checklist_form})

def add_checklist(request, monster_id):
  form = ChecklistForm(request.POST)
  if form.is_valid():
    new_checklist = form.save(commit=False)
    new_checklist.monster_id = monster_id
    new_checklist.save()
  return redirect('monster-detail', monster_id=monster_id)