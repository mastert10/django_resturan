from msilib import type_binary
from unicodedata import category
from django.db import models
from django.forms import ImageField
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils import timezone



# Create your models here.
class Chefs(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگی' ,max_length=200)
    slug = models.SlugField(verbose_name='ادرس اشپز')
    age = models.IntegerField(verbose_name='سن')
    
    class Meta: 
        verbose_name = 'سرآشپز'
        verbose_name_plural = 'سرآشپز ها'
    
    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self', default=None , null=True , blank=True , on_delete=models.SET_NULL, related_name='children',verbose_name='زیردسته')
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(verbose_name="ادرس دسته بندی")
    published = models.DateTimeField(auto_now_add=True , auto_now=False, verbose_name="تاریخ انتشار")
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
      
    def __str__(self):
        return self.title
    

    
class Food(models.Model):
    FOOD_CHOICES = (
        ("pitza",'پیتزا' ),
        ("sandwich",'ساندویچ'),
        ("dessert",'دسر'),
        ('all','همه'),
    )
    name = models.CharField(max_length=200 ,verbose_name='نام غذا' )
    description = models.TextField(_('توضیحات'))
    thumbnail = models.ImageField(_('عکس'), upload_to='images/')
    price = models.IntegerField(_('قیمت'))
    category = models.ManyToManyField('Category',verbose_name='دسته بندی', related_name='foods')
    rate = models.IntegerField(default=0 ,verbose_name="امتیاز")
    chef = models.ForeignKey('Chefs',on_delete=models.SET_NULL, null=True ,verbose_name="سرآشپز")
    time = models.IntegerField(verbose_name="زمان لازم")
    type_food = models.CharField(max_length=10, choices=FOOD_CHOICES , verbose_name='نوع غذا', default='all')
    pub_date = models.DateField(default=timezone.now,verbose_name="تاریخ انتشار")
    
    class Meta: 
        verbose_name = 'لیست غذا'
        verbose_name_plural = 'لیست غذا ها'
        
    def get_absolute_url(self):
        return reverse("account:home")
    
    
    def __str__(self):
        return self.name
    
    def category_to_str(self):
        return ", ".join([category.title for category in self.category.all()])
    # category_to_str.short_description = 'دسته بندی'
