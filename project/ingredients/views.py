from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Food

from project.recipes.models import Recipe
from .forms import FoodCreateForm

@login_required
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
                ingredient_to_remove_id = request.POST['remove_items']
                if ingredient_to_remove_id == "RemoveAll":
                    ingobjs = Food.objects.all()
                    for ingobj in ingobjs:
                        ingobj.users.remove(request.user.id)
                else: 
                    ing = Food.objects.filter(fd_id=ingredient_to_remove_id).first()
                    ing.users.remove(request.user.id).save()
            except:
                pass
        
        if "add_items" in request.POST:
            food_name = request.POST["add_items"]
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

def autocomplete(request):
    print("auto")
    if "term" in request.GET:
        query_res = Food.objects.filter(scientific_name__istartswith=request.GET.get("term"))
        ingredient_list = []
        for i in query_res:
            ingredient_list.append(i.scientific_name)
        
        return JsonResponse(ingredient_list, safe=False)
    
    return redirect(ingredient_index_view)


def ingredient_update_view(request):
    pass

def ingredient_deleteAll_view(request):
    try:
        Food.objects.all().delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect(ingredient_index_view)