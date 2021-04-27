from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from project.recipes.models import Recipe, RecipeFood
from project.ingredients.models import Food, UserFood


# This page should show the user what recipes he can make after going shopping.
# The view should also show the shoppinglist itself.

# Show recipes that the user cannot make with their in_pantry ingredients

@login_required
def shoppinglist_view(request):
    if request.method == "POST":
        print(request.POST)

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

    return render(request, "pages/shoppinglist.html", {"recipes": recipe_list, "shopping_list": shopping_list})


def mark_userfood_bought(userfood_id, request):
    # Get userfood object with in_pantry=False
    userfood_shoppinglist_obj = UserFood.objects.filter(id=userfood_id).first()
    qty = userfood_shoppinglist_obj.qty

    # Get userfood object with in_pantry=True
    # If it doesn't exist, create it
    food_obj = userfood_shoppinglist_obj.food
    userfood_pantry_obj = UserFood.objects.filter(food=food_obj, user=request.user, in_pantry=True).first()

    if userfood_pantry_obj is None:
        userfood_pantry_obj = UserFood.objects.create(food=food_obj, user=request.user, qty=qty, in_pantry=True)
        userfood_pantry_obj.save()

    
    else:
        userfood_pantry_obj.qty += qty
        userfood_pantry_obj.save()
    
    # Delete shopping list entry
    userfood_shoppinglist_obj.delete()


    # Add pantry entry

def update_user_food_qty(user, food, qty, in_pantry):
    userfood_obj = UserFood.objects.filter(user=user, food=food, in_pantry=in_pantry).first()
    userfood_obj.qty = qty
    userfood_obj.save()


def update_userfood_qty(userfood_id, qty):
    userfood_obj = UserFood.objects.filter(id=userfood_id).first()
    userfood_obj.qty = qty
    userfood_obj.save()



def get_shopping_list(request):
    shopping_list = UserFood.objects.filter(user=request.user, in_pantry=False)
    return shopping_list


# Return all recipes that the user cannot make with their ingredients.
# But can make after buying everything on the shopping list.
def get_recipe_list(request):

    all_recipes = Recipe.objects.all()
    # For each recipe
    for recipe in all_recipes:
        recipe_ingredients = recipe.foods.all()

        # For ingredient in recipe
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
            
            # If user is already able to make this recipe,
            # or if user cannot make it even after buying the entire shopping list, remove it.
            if not pantry_qty <= required_qty <= pantry_qty + shopping_list_qty:
                # Remove recipe
                all_recipes = all_recipes.exclude(name=recipe.name)

    return all_recipes


# This function will mark all ingredients in the shopping list as having been bought
def buy_shopping_list(request):
    pass