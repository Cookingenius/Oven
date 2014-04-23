from django.contrib import admin
from .models import Category, Food


class FoodAdmin(admin.ModelAdmin):
    list_filter = ('category',)


admin.site.register(Category)
admin.site.register(Food, FoodAdmin)
