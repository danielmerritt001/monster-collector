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
    path('banes/create/', views.BaneCreate.as_view(), name='bane-create'),
    path('banes/<int:pk>/', views.BaneDetail.as_view(), name='bane-detail'),
    path('banes/', views.BaneList.as_view(), name='bane-index'),
    path('banes/<int:pk>/update/', views.BaneUpdate.as_view(), name='bane-update'),
    path('banes/<int:pk>/delete/', views.BaneDelete.as_view(), name='bane-delete'),
]
