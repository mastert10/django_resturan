from pickle import FALSE
from random import choices
from tabnanny import verbose
from django.db import models
from django.forms import CharField

# Create your models here.
class reservation(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=256,verbose_name='ایمیل')
    phone = models.CharField(max_length=200,verbose_name='تلفن')
    number = models.IntegerField(verbose_name='تعداد')
    date = models.DateField(auto_now=False , auto_now_add=False,verbose_name='تاریخ حضور')
    time = models.TimeField(auto_now=False , auto_now_add=False,verbose_name='زمان حضور')
    
    class Meta:
        verbose_name='لیست رزرو '
        verbose_name_plural = 'لیست رزرو ها'
        
    
    def __str__(self):
        return self.email


