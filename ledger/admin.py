from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, Profile, RecipeImage
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class Admin(UserAdmin):
    inlines = [
        ProfileInLine,
    ]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeIngredientInline,
        RecipeImageInLine,
    ]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, Admin)
