from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Recipe
import json


def markers_as_json():
    recipes = Recipe.objects.order_by('-date')
    return json.dumps([
        {
            "position": {
                "lat": recipe.location.latitude,
                "lng": recipe.location.longitude,
            },
            "url": reverse('cook:recipe', args=(recipe.slug, )),
        }
        for recipe in recipes
    ])


def index(request):
    recipes = Recipe.objects.order_by('-date')
    return render(request, 'cook/index.html', {
        'recipes': recipes,
        'markers': markers_as_json(),
    })


def recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'cook/recipe.html', {
        'recipe': recipe,
        'markers': markers_as_json(),
    })
