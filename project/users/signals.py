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
        create_recipes()
post_save.connect(view_signal, sender=User)

def create_recipes():
    food_list = ['garlic', 'lemon', 'ground pepper', 'whipped cream', 'oil', 'butter',
                'spaghetti', 'wheat flour', 'sugar', 'milk', 'egg', 'baking soda']
    amount_list = ['1.00','1.00','0.50', '1.50', '1.00', '50.00', '400.00', '4.00',
                    '5.00', '4.00', '3.00', '0.00']
    unit_list   = ['clove', 'pcs', 'ts', 'dl', 'tbsp', 'g', 'g', 'dl', 'tbsp', 'dl',
                    'pcs', 'tbsp']

    assert(len(food_list) == len(amount_list))
    assert(len(amount_list) == len(unit_list))

    recipes_recipe_1_name = 'Pasta al limone'
    recipes_recipe_1_description = 'Lemon pasta, or pasta limone, is a simple pasta dish with a clear taste of fresh lemon. This popular pasta dish can be made both with and without cream, and here you have the cream variant - creamy and fresh! You can make this dish with dried pasta, but if you are going to put an extra tip on it, you make it with homemade pasta. Served alone as a light lunch or as an accompaniment to chicken or white fish.'
    recipes_recipe_1_rating = 4
    recipes_recipe_1_prep_time = 20
    recipes_recipe_1_instruction = '1. Put garlic, lemon peel and pepper together with oil in a pan. Cook over medium heat until the onion is shiny. Add cream and stir in butter. Let the cream sauce simmer on low to medium heat while you cook the pasta.\r\n\r\n2. Boil a large pot of water and add salt. Put the pasta in the boiling water. If you use dried pasta, you can cook it until there are 1-2 minutes left of the cooking time, and if you use fresh pasta, you only need to cook it for 30 seconds - 1 minute. The pasta should not be completely finished, as it should also soak in the sauce.\r\n\r\n3. Turn the pasta into the sauce, and take care of the pasta water. Add lemon juice. Feel free to start with half the amount of lemon juice and add little by little, until you think it is sour enough.\r\n\r\n4. Turn in the parmesan and parsley, and let the pasta soak in the sauce until the pasta is cooked through. Dilute with a little pasta water while the pasta soaks. The pasta water helps to thin out the consistency of the sauce and add a delicious taste. Turn in the parmesan and parsley, and let the pasta soak in the sauce until the pasta is cooked through. Dilute with a little pasta water while the pasta soaks. The pasta water helps to thin out the consistency of the sauce and add a delicious taste.'
    recipes_recipe_1_servings = 4
    recipes_recipe_1_image = 'recipes/Pasta_al_limone.jpg'
    recipes_recipe_1_link = 'https://www.matprat.no/oppskrifter/kos/pasta-al-limone/'


    recipes_recipe_2_name = 'Waffles'
    recipes_recipe_2_description = 'Waffles, a success for both young and old. Set out jams, sour cream, butter, sugar and brown cheese, then you are guaranteed that everyone will have their wishes fulfilled. Try our delicious waffle recipe!'
    recipes_recipe_2_rating = 3
    recipes_recipe_2_prep_time = 40
    recipes_recipe_2_instruction = '1. Put everything dry in a bowl and dilute with a little of the milk at a time. Stir well between each time to get a smooth mixture without lumps of milk.\r\n\r\n2. Stir in the eggs and add the melted butter. Let the batter swell for 1/2 hour. Adjust the batter with a little water or milk if it is too thick.\r\n\r\n3. Bake the waffles and serve them hot'
    recipes_recipe_2_servings = 1
    recipes_recipe_2_image = 'recipes/Waffles.jpeg'
    recipes_recipe_2_link = 'https://www.matprat.no/oppskrifter/tradisjon/vafler/'

    recipe_1 = Recipe.objects.create(name = recipes_recipe_1_name, description = recipes_recipe_1_description,
                                    rating = recipes_recipe_1_rating, prep_time = recipes_recipe_1_prep_time,
                                    instruction = recipes_recipe_1_instruction, servings = recipes_recipe_1_servings,
                                    image = recipes_recipe_1_image, link = recipes_recipe_1_link)
    recipe_2 = Recipe.objects.create(name = recipes_recipe_2_name, description = recipes_recipe_2_description,
                                    rating = recipes_recipe_2_rating, prep_time = recipes_recipe_2_prep_time,
                                    instruction = recipes_recipe_2_instruction, servings = recipes_recipe_2_servings,
                                    image = recipes_recipe_2_image, link = recipes_recipe_2_link)
    food_objects = []
    ingredient_objects = []
    for counter, food_name in enumerate(food_list):
        food_object = Food.objects.create(name=food_name)
        food_object.save()
        ingredient_object = Ingredient.objects.create(food=food_object, amount=amount_list[counter], unit = unit_list[counter])
        ingredient_object.save()
        ingredient_objects.append(ingredient_object)

    for i in range(0,7):
        recipe_1.ingredients.add(ingredient_objects[i])
    for i in range(7,11):
        recipe_2.ingredients.add(ingredient_objects[i])

    recipe_1.save()
    recipe_2.save()
        








