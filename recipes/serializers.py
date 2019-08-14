from rest_framework import serializers
from .models import FoodRecipe, Project, Post


class FoodRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodRecipe
        fields = ('title', 'description', 'image',)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'description', 'image',)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'created_at', 'updated_at')
