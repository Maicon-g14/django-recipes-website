from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipe-create"),
    path('about', views.about, name="recipes-about"),
]