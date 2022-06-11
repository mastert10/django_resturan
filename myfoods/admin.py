from django.contrib import admin

from myfoods.models import Food, Chefs, Category
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display= ("name", "price","pub_date", "type_food","category_to_str")
    list_filter = ('type_food',)
    search_fields = ('title' , 'slug')
    
admin.site.register(Food,FoodAdmin)
admin.site.register(Chefs)
admin.site.register(Category)


