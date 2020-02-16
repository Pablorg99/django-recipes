from django.urls import path
from . import views

URL_PATTERNS = [
    path('recipes', views.ListRecipes.as_view()),
    path('recipe/<int:pk>/', views.DetailRecipe.as_view()),
    path('ingredients', views.ListIngredients.as_view()),
    path('ingredient/<int:pk>', views.DetailIngredient.as_view())
]
