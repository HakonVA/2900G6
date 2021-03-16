from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages


from .models import Food

from project.recipes.models import Recipe
from .forms import FoodCreateForm

def ingredient_index_view(request):
    """[summary]

    Args:
        request ([type]): [description]

    Raises:
        Http404: [description]

    Returns:
        [type]: [description]
    """

    if request.method == "POST":
        if "remove_items" in request.POST:
            try:
                ingredient_to_remove_name = request.POST['remove_items']
                ing = Food.objects.filter(scientific_name=ingredient_to_remove_name).first()
                ing.users.remove(request.user.id).save()
            except:
                pass
        
        if "scientific_name" in request.POST:
            food_name = request.POST["scientific_name"]
            if food_name is not None:
                food_obj = Food.objects.filter(scientific_name=food_name)
                if food_obj is not None:
                    # Hacky. TODO: fix.
                    try:
                        food_obj.first().users.add(request.user.id)
                    except:
                        messages.error(request, "%s does not exist in our database" % food_name)


    form = None

    obj = Food.objects.filter(users=request.user.id)

    recipes = get_recipes(obj)

    return render(request, "pages/ingredients.html", {"objects": obj, "form": form, "recipes": recipes})

def get_recipes(ingredients):
    # We want to return the set of recipes such that each recipe's
    # ingredients are contained in the user's ingredient table

    # This is a hacky solution
    compl_ingredients = Food.objects.exclude(fd_id__in=ingredients)
    test = Recipe.objects.exclude(req_ingredients__in=compl_ingredients)
    return test


def ingredient_update_view(request):
    pass

def ingredient_deleteAll_view(request):
    try:
        Food.objects.all().delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect(ingredient_index_view)