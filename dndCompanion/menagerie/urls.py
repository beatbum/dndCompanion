from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_menagerie,name='view_menagerie'),
    path('add-monster/',views.add_monster,name='add_monster'),
    path('<str:name>/',views.view_monster,name='view_monster'),
]
