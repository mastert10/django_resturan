from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# Create your models here.    
class Article(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان مقاله')
    slug = models.SlugField(verbose_name='ادرس مقاله' ,null=True)
    descirption = models.CharField(max_length=200 , verbose_name='توضیحات')
    content = models.TextField(verbose_name='متن')
    author = models.ForeignKey(User ,verbose_name='نویسنده', on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="blog/", verbose_name='عکس')
    created = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ساخت')
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
    
    def __str__(self):
        return self.title
        

    
    
    
    
    
    
