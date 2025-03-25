from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe
from .forms import RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'recipe_list'


def recipe_add(request):
    form = RecipeForm
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            t = Recipe()
            t.name = form.cleaned_data.get('name')
            t.author = form.cleaned_data.get('author')
            t.ingredients = form.cleaned_data.get('ingredients')
            t.quantity = form.cleaned_data.get('quantity')
            t.image = form.cleaned_data.get('image')
            t.save()

    ctx = {}
    return render(request, 'recipe_add.html', ctx)


class RecipeCreateView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_add.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
