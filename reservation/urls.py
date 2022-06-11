from django.urls import path
from .views import Reserve

app_name='reserve'
urlpatterns = [
    path('', Reserve, name='home')
    
]
