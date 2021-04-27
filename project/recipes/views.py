from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Recipe, RecipeFood
from project.ingredients.models import Food, UserFood
from project.shoppinglist.views import mark_userfood_bought

# This page should show the user the recipes that they cannot make, even after buying the entire shopping list.
# It should allow them to add the necessary ingredients to their shopping list.

@login_required
def recipe_view(request):

    if request.method == "POST":
        if "add_recipe" in request.POST:
            rc_id = int(request.POST["add_recipe"])
            add_recipe_to_shopping_list(rc_id, request)

        if "adjust_qty" in request.POST:
            target_food_id = int(request.POST["adjust_qty_food"])
            new_qty = int(request.POST["adjust_qty"])
            user_food_obj = UserFood.objects.filter(id=target_food_id).first()
            user_food_obj.qty = new_qty
            user_food_obj.save()
        
        if "remove_items" in request.POST:
            if request.POST["remove_items"] == "RemoveAll":
                userfoods = UserFood.objects.filter(user=request.user, in_pantry=False)
                userfoods.all().delete()
                
            else:
                id_to_remove = int(request.POST["remove_items"])
                userfood = UserFood.objects.filter(id=id_to_remove)
                userfood.all().delete()


        if "mark_as_bought" in request.POST:
            userfood_id = request.POST["mark_as_bought"]
            if userfood_id == "mark_all":
                userfoods = UserFood.objects.filter(user=request.user, in_pantry=False)
                for userfood in userfoods:
                    mark_userfood_bought(userfood.id, request)
            else:
                mark_userfood_bought(int(userfood_id), request)

    form = None

    userfood_list = UserFood.objects.filter(user=request.user, in_pantry=False).order_by("food")
    food_list = Food.objects.filter(userfood__in=userfood_list).order_by("fd_id")
    shopping_list = list(zip(food_list, userfood_list))



    recipe_list = get_recipe_list(request)

    return render(request, "pages/recipes.html", {"recipes": recipe_list, "shopping_list": shopping_list})





def get_recipe_list(request):
    # Find every recipe that the user cannot make, even considering the shopping list

    recipes = Recipe.objects.all()
    print(recipes)

    for recipe in recipes:
        # for each ingredient in recipe
        recipe_ingredients = recipe.foods.all()

        for ingredient in recipe_ingredients:
            recipefood = RecipeFood.objects.filter(recipe=recipe, food=ingredient).first()
            required_qty = recipefood.qty

            pantry_qty = UserFood.objects.filter(user=request.user, food=ingredient, in_pantry=True).first()
            if pantry_qty is None:
                pantry_qty = 0
            else:
                pantry_qty = pantry_qty.qty

            shopping_list_qty = UserFood.objects.filter(user=request.user, food=ingredient, in_pantry=False).first()
            if shopping_list_qty is None:
                shopping_list_qty = 0
            else:
                shopping_list_qty = shopping_list_qty.qty
            
            print("%s, %s, %s" % (pantry_qty, shopping_list_qty, required_qty))
            if pantry_qty + shopping_list_qty >= required_qty:
                recipes = recipes.exclude(name=recipe.name)

    print(recipes)
    return recipes



def add_recipe_to_shopping_list(rc_id, request):
    recipe_obj = Recipe.objects.filter(rc_id=rc_id).first()
    ingredients = recipe_obj.foods.all()

    # For each ingredient in recipe
    for ingredient in ingredients:
        print(ingredient)

        recipefood = RecipeFood.objects.filter(recipe=recipe_obj, food=ingredient).first()
        required_qty = recipefood.qty

        pantry_qty = UserFood.objects.filter(user=request.user, food=ingredient, in_pantry=True).first()
        if pantry_qty is None:
            pantry_qty = 0
        else:
            pantry_qty = pantry_qty.qty

        shopping_list_qty = UserFood.objects.filter(user=request.user, food=ingredient, in_pantry=False).first()
        if shopping_list_qty is None:
            shopping_list_qty = 0
        else:
            shopping_list_qty = shopping_list_qty.qty

        # Find the difference between what the user has, and what they need

        difference = required_qty - (pantry_qty + shopping_list_qty)

        # Check if we need to add more to the shopping list
        if difference > 0:
            # If ingredient does not already exist in the user's shopping list, create it

            if shopping_list_qty == 0:
                uf = UserFood.objects.create(user=request.user, food=ingredient, qty=difference, in_pantry=False)
                uf.save()
            else:
                uf = UserFood.objects.filter(user=request.user, food=ingredient, in_pantry=False).first()
                uf.qty += difference
                uf.save()



