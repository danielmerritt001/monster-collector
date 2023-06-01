from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Monster, Bane
from .forms import ChecklistForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# classes

class Home(LoginView):
  template_name = 'home.html'

class MonsterCreate(CreateView):
  model = Monster
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

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

def about(request):
  return render(request, 'about.html')

def monster_index(request):
  monsters = Monster.objects.filter(user=request.user)
  return render(request, 'monsters/index.html', {'monsters': monsters})

def monster_detail(request, monster_id):
  monster = Monster.objects.get(id=monster_id)
  banes_monster_doesnt_have = Bane.objects.exclude(id__in = monster.banes.all().values_list('id'))
  checklist_form=ChecklistForm()
  return render(request, 'monsters/detail.html', { 'monster': monster, 'checklist_form': checklist_form, 'banes': banes_monster_doesnt_have})

def add_checklist(request, monster_id):
  form = ChecklistForm(request.POST)
  if form.is_valid():
    new_checklist = form.save(commit=False)
    new_checklist.monster_id = monster_id
    new_checklist.save()
  return redirect('monster-detail', monster_id=monster_id)

def assoc_bane(request, monster_id, bane_id):
  Monster.objects.get(id=monster_id).banes.add(bane_id)
  return redirect('monster-detail', monster_id=monster_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('monster-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)