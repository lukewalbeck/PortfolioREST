from django.db import models

# Create your models here.
class FoodRecipe(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="img", default='')

    def __str__(self):
        return self.title