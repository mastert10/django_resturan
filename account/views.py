from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView ,CreateView , UpdateView
from myfoods.models import Food ,Chefs
from reservation.models import reservation
from .mixins import FieldMixin


# Create your views here.
@login_required
def Home(request):
    food_list = Food.objects.all()
    chefs = Chefs.objects.all()
    reserve = reservation.objects.all()
    
    context = {
        'foods' : food_list,
        'chefs' : chefs,
        'reserves' : reserve,
    }
    return render(request, 'registration/home.html',context)
    

class FoodCraete(LoginRequiredMixin,FieldMixin,CreateView):  
    model = Food 
    template_name = 'registration/food_create_update.html'


class FoodUpdate(LoginRequiredMixin,FieldMixin,UpdateView):
    model=Food
    template_name = 'registration/food_create_update.html'