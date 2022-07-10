from django.contrib import admin
from .models import Category

class Category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name', 'slug')
    
# Register your models here.
admin.site.register(Category, Category_admin)