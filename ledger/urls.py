from django.urls import path

from .views import recipe_list

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe-list')
]

app_name = "ledger"