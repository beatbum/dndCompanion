from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='encounter_home'),
]
