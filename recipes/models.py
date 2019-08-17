from django.db import models

# Create your models here.
class FoodRecipe(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="img", default='')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="img", default='')
    github = models.URLField(blank=True, default='')
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="img", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title