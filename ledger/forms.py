from django import forms
# from .models import TaskGroup


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    # ingredients = forms.CharField(max_length=100)
    # quantity = forms.IntegerField()
    # image = forms.ImageField()
