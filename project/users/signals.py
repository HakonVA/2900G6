from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from project.recipes.models import Food, Ingredient, Recipe

#is connected with post_save which fetches saves from all models in app "users"
#on create user:
    #checks if already a database established, if not
        #creates some entries in the create_recipes method
def view_signal(sender, instance, created, raw, **kwargs):
    users_objects = User.objects.all()
    if created and not raw and len(users_objects) <= 1:
        populate_foods()
        #create_recipes()
        more_recipes()
post_save.connect(view_signal, sender=User)

def populate_foods():
    food_file = open("project/users/populate_food.txt", "r")
    for line in food_file:
        new_food = Food.objects.create(name = line)
        new_food.save
    food_file.close()
        
def more_recipes():
    num_recipes = 6
    text_file = open("project/users/populate_recipe.txt", "r")
    for i in range(1, num_recipes+1): #recipe 1,2,3,4,5,6
        
        text_file.read(len("name_x:"))
        recipe_name = text_file.readline()
        
        text_file.read(len("description:"))
        recipe_description = text_file.readline() 
        
        text_file.read(len("rating:"))
        recipe_rating = text_file.readline()

        text_file.read(len("prep_time:"))
        recipe_prep_time = text_file.readline()

        text_file.read(len("instruction:"))
        recipe_instruction = ""
        last_pos = text_file.tell()
        while (text_file.read(len("servings:")) != "servings:"):
            text_file.seek(last_pos)
            recipe_instruction += text_file.readline()
            last_pos = text_file.tell()

        recipe_servings = text_file.readline()
        
        text_file.read(len("image:"))
        recipe_image = "recipes/" + text_file.readline().split()[0] + ".webp"
        
        text_file.read(len("link:"))
        recipe_link = text_file.readline()

        new_recipe = Recipe.objects.create(
            
            name = recipe_name, description = recipe_description,
            rating = recipe_rating, prep_time = recipe_prep_time, 
            instruction = recipe_instruction, servings = recipe_servings, 
            image = recipe_image, link = recipe_link
            
        )

        text_file.readline() #between ingredients

        ingredient_line = text_file.readline()
        while (ingredient_line != "\n" or ingredient_line == "end"):
            recipe_amount = ""
            recipe_unit = ""
            recipe_food_name = ""
            ingredient_line = ingredient_line.split()
            recipe_amount   = ingredient_line[0]
            recipe_unit     = ingredient_line[1]

            for i in range(2, len(ingredient_line)):
                recipe_food_name += ingredient_line[i]
                recipe_food_name += " "   
                                
            try: 
                food_type = Food.objects.get(name = recipe_food_name)
            except:
                    food_type = Food.objects.create(name=recipe_food_name)
                    food_type.save()

            ingredient_object = Ingredient.objects.create(food = food_type, unit = recipe_unit, amount = recipe_amount)
            ingredient_object.save()
            new_recipe.ingredients.add(ingredient_object)
            ingredient_line = text_file.readline()


        new_recipe.save()

    text_file.close()