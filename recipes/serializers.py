from rest_framework import serializers
from .models import FoodRecipe, Project


class FoodRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodRecipe
        fields = ('title', 'description', 'image',)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'description', 'image',)
