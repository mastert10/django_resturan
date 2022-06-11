from multiprocessing import context
from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import Category, Food 


# Create your views here.
def Food_List(request):
    #global categorys 
    categorys = Category.objects.all()
    food_list = Food.objects.all()
    
    context = {
        "foods" : food_list,
        'Categories':categorys,
    }
    return render(request,"myrest/home.html",context)


def Food_Detail(request, id):
    
    context = {
        'food' :get_object_or_404(Food , id=id),
        'resent_foods': Food.objects.order_by('pub_date')[:5],
        'categories':Category.objects.all()
    }
    return render(request, 'myrest/detail.html',context)

def Category_List(request , slug):
    category_list = get_object_or_404(Category , slug=slug)
    context = {
        'categories':category_list,
    }
    return render (request , 'myrest/category.html' , context)

def Search(request):
    if request.method == "GET":
        src = request.GET.get("search")
    food_list = Food.objects.filter(name__icontains=src)
    context = {
        "articles":food_list,
    }
    return render(request, "blog/home.html", context)

