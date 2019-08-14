from django.contrib import admin
from .models import FoodRecipe, Project, Post
# Register your models here.
admin.site.register(FoodRecipe)
admin.site.register(Project)
admin.site.register(Post)
