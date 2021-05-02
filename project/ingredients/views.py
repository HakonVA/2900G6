from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Food, UserFood

from project.recipes.models import Recipe, RecipeFood
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
        print(request.POST)

        # User adds ingredient
        if "add_items" in request.POST:
            food_name = request.POST["add_items"]
            qty_to_add = int(request.POST["add_items_qty"])
            if food_name is not None:
                food_obj = Food.objects.filter(scientific_name=food_name).first()
                if food_obj is not None:
                    try:
                        uf = UserFood.objects.create(user=request.user, food=food_obj, qty=qty_to_add, in_pantry=True)
                        uf.save()
                    except:
                        messages.error(request, "%s does not exist in our database" % food_name)
    
        # User adjusts ingredient quantity
        if "adjust_qty_food" in request.POST:

            userfood_id = int(request.POST["adjust_qty_food"])
            userfood_qty = int(request.POST["adjust_qty"])

            user_food_obj = UserFood.objects.filter(id=userfood_id).first()
            user_food_obj.qty = userfood_qty
            user_food_obj.save()

        # User removes ingredient(s)
        if "remove_items" in request.POST:
            
            userfood_id = request.POST['remove_items']
            if userfood_id == "RemoveAll":
                userfood_objs = UserFood.objects.filter(user=request.user, in_pantry=True)
                userfood_objs.all().delete()
            else:
                userfood_obj = UserFood.objects.filter(id=int(userfood_id))
                userfood_obj.all().delete()


    form = None

    obj2 = UserFood.objects.filter(user=request.user, in_pantry=True).order_by("food")
    obj = Food.objects.filter(userfood__in=obj2).order_by("fd_id")

    recipes = get_ingredients_recipe_list(request)

    return render(request, "pages/ingredients.html", {"objects": list(zip(obj, obj2)), "form": form, "recipes": recipes})

def get_ingredients_recipe_list(request):

    userfoods = UserFood.objects.filter(user=request.user, in_pantry=True).order_by("food")

    # First, deselect all recipes for which the user doesn't have the ingredient.
    complement_ingredients = Food.objects.exclude(userfood__in=userfoods)
    available_recipes = Recipe.objects.exclude(foods__in=complement_ingredients)

    if available_recipes.first() is None:
        return [] 

    # Then deselect the recipes for which the user has the ingredient, but not the necessary quantity.
    recipe_ids_to_remove = []
    for recipe in available_recipes:
        # check if the user has all ingredients in required amount
        for recipefood in RecipeFood.objects.filter(food__in=recipe.foods.all()):
            if userfoods.filter(food=recipefood.food, in_pantry=True).first() is None:
                break
            if recipefood.qty > userfoods.filter(food=recipefood.food, in_pantry=True).first().qty:
                recipe_ids_to_remove.append(recipefood.recipe.rc_id)
                break

    available_recipes = available_recipes.exclude(rc_id__in=recipe_ids_to_remove)
    return available_recipes


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