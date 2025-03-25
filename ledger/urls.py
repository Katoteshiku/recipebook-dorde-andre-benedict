from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/add', RecipeCreateView.as_view(), name='add-recipe'),
]

app_name = "ledger"
