from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes(request):
    recipes = [i for i in DATA.keys()]
    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)

def recipe(request):
    recipe_name = request.GET.get("name")
    servings = int(request.GET.get("servings", 1))
    ingridients_dict = {}
    

    for recipe, ingridients in DATA.items():
        if recipe == recipe_name:
            for ingridient, serving in ingridients.items():
                serving = serving * servings
                ingridients_dict[ingridient] = serving

    context = {
        'recipe_name': recipe_name,
        'ingridients': ingridients_dict
    }
    return render(request, 'recipe.html', context)

