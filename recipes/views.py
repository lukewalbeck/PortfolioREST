from django.shortcuts import render
from rest_framework import generics
from .models import FoodRecipe, Project
from .serializers import FoodRecipeSerializer, ProjectSerializer
# Create your views here.

class FoodRecipeList(generics.ListCreateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer


class FoodRecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
