from django.contrib import admin

# Register your models here.
from .models import Category

class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('Category_name',)}

    list_display=('Category_name','slug')

admin.site.register(Category,Categoryadmin)