from django.urls import path
from . import views


app_name='blog'
urlpatterns = [
    path('',views.Home, name='home'),
    path('<slug:slug>/',views.Detail, name='detail'),
    path('search/',views.Search, name='search'),
]



