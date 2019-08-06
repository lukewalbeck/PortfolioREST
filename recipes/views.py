from django.shortcuts import render
from rest_framework import generics
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer
# Create your views here.

class FoodRecipeList(generics.ListCreateAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer


class FoodRecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodRecipe.objects.all()
    serializer_class = FoodRecipeSerializer