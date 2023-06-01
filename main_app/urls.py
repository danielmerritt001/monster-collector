from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('monsters/', views.monster_index, name='monster-index'),
    path("monsters/<int:monster_id>/", views.monster_detail, name="monster-detail"),
    path('monsters/create/', views.MonsterCreate.as_view(), name='monster-create'),
    path('monsters/<int:pk>/update/', views.MonsterUpdate.as_view(), name='monster-update'),
    path('monsters/<int:pk>/delete/', views.MonsterDelete.as_view(), name='monster-delete'),
    path('monsters/<int:monster_id>/add-checklist', views.add_checklist, name='add-checklist'),
]
