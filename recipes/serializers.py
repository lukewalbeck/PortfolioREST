from rest_framework import serializers
from .models import FoodRecipe, Project, Post


class FoodRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodRecipe
        fields = ('id', 'title', 'description', 'image',)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'image',)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'created_at', 'updated_at')
