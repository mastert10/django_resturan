from django import template
from ..models import Category


register = template.Library()

@register.simple_tag
def title():
    return "مای وبلاگ"


@register.inclusion_tag("myrest/partials/category_navbar.html")
def category_navbar():
    return {
        'Categories' : Category.objects.all()
    }





    
    
