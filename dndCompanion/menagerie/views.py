from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Monster
# Need a view for adding monster type
def add_monster(request):
    return HttpResponse("This is where you would create new monsters")

# Need a view for seeing all different types of monsters by name
def view_menagerie(request):
    monsters = Monster.objects.order_by("name")
    context = {"monster_list": monsters}
    return render(request,"menagerie/view_menagerie.html",context)

# Need to view stats for individual monsters
def view_monster(request,name):
    return HttpResponse("This is where a display of the chosen monster would be")
