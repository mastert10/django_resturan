from django.urls import path
from .views import Food_List, Food_Detail , Category_List , Search


app_name = 'foods'
urlpatterns = [
    path('', Food_List , name='home'),
    path('<int:id>/', Food_Detail , name='detail'),
    path('cat/<slug:slug>', Category_List , name='category'),
    path('search/',Search, name='search'),
]

