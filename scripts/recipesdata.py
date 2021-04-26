#!/usr/bin/env python


# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript recipes
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: project.recipes.models.Food

    from project.recipes.models import Food

    recipes_food_1 = Food()
    recipes_food_1.name = 'garlic'
    recipes_food_1 = importer.save_or_locate(recipes_food_1)

    recipes_food_2 = Food()
    recipes_food_2.name = 'lemon'
    recipes_food_2 = importer.save_or_locate(recipes_food_2)

    recipes_food_3 = Food()
    recipes_food_3.name = 'ground pepper'
    recipes_food_3 = importer.save_or_locate(recipes_food_3)

    recipes_food_4 = Food()
    recipes_food_4.name = 'whipped cream'
    recipes_food_4 = importer.save_or_locate(recipes_food_4)

    recipes_food_5 = Food()
    recipes_food_5.name = 'oil'
    recipes_food_5 = importer.save_or_locate(recipes_food_5)

    recipes_food_6 = Food()
    recipes_food_6.name = 'butter'
    recipes_food_6 = importer.save_or_locate(recipes_food_6)

    recipes_food_7 = Food()
    recipes_food_7.name = 'spaghetti'
    recipes_food_7 = importer.save_or_locate(recipes_food_7)

    recipes_food_8 = Food()
    recipes_food_8.name = 'wheat flour'
    recipes_food_8 = importer.save_or_locate(recipes_food_8)

    recipes_food_9 = Food()
    recipes_food_9.name = 'suger'
    recipes_food_9 = importer.save_or_locate(recipes_food_9)

    recipes_food_10 = Food()
    recipes_food_10.name = 'milk'
    recipes_food_10 = importer.save_or_locate(recipes_food_10)

    recipes_food_11 = Food()
    recipes_food_11.name = 'egg'
    recipes_food_11 = importer.save_or_locate(recipes_food_11)

    recipes_food_12 = Food()
    recipes_food_12.name = 'baking soda'
    recipes_food_12 = importer.save_or_locate(recipes_food_12)

    # Processing model: project.recipes.models.Ingredient

    from project.recipes.models import Ingredient

    recipes_ingredient_1 = Ingredient()
    recipes_ingredient_1.food = recipes_food_1
    recipes_ingredient_1.amount = Decimal('1.00')
    recipes_ingredient_1.unit = 'clove'
    recipes_ingredient_1 = importer.save_or_locate(recipes_ingredient_1)

    recipes_ingredient_2 = Ingredient()
    recipes_ingredient_2.food = recipes_food_2
    recipes_ingredient_2.amount = Decimal('1.00')
    recipes_ingredient_2.unit = 'pcs'
    recipes_ingredient_2 = importer.save_or_locate(recipes_ingredient_2)

    recipes_ingredient_3 = Ingredient()
    recipes_ingredient_3.food = recipes_food_3
    recipes_ingredient_3.amount = Decimal('0.50')
    recipes_ingredient_3.unit = 'ts'
    recipes_ingredient_3 = importer.save_or_locate(recipes_ingredient_3)

    recipes_ingredient_4 = Ingredient()
    recipes_ingredient_4.food = recipes_food_4
    recipes_ingredient_4.amount = Decimal('1.50')
    recipes_ingredient_4.unit = 'dl'
    recipes_ingredient_4 = importer.save_or_locate(recipes_ingredient_4)

    recipes_ingredient_5 = Ingredient()
    recipes_ingredient_5.food = recipes_food_5
    recipes_ingredient_5.amount = Decimal('1.00')
    recipes_ingredient_5.unit = 'tbsp'
    recipes_ingredient_5 = importer.save_or_locate(recipes_ingredient_5)

    recipes_ingredient_6 = Ingredient()
    recipes_ingredient_6.food = recipes_food_6
    recipes_ingredient_6.amount = Decimal('50.00')
    recipes_ingredient_6.unit = 'g'
    recipes_ingredient_6 = importer.save_or_locate(recipes_ingredient_6)

    recipes_ingredient_7 = Ingredient()
    recipes_ingredient_7.food = recipes_food_7
    recipes_ingredient_7.amount = Decimal('400.00')
    recipes_ingredient_7.unit = 'g'
    recipes_ingredient_7 = importer.save_or_locate(recipes_ingredient_7)

    recipes_ingredient_8 = Ingredient()
    recipes_ingredient_8.food = recipes_food_8
    recipes_ingredient_8.amount = Decimal('4.00')
    recipes_ingredient_8.unit = 'dl'
    recipes_ingredient_8 = importer.save_or_locate(recipes_ingredient_8)

    recipes_ingredient_9 = Ingredient()
    recipes_ingredient_9.food = recipes_food_9
    recipes_ingredient_9.amount = Decimal('5.00')
    recipes_ingredient_9.unit = 'tbsp'
    recipes_ingredient_9 = importer.save_or_locate(recipes_ingredient_9)

    recipes_ingredient_10 = Ingredient()
    recipes_ingredient_10.food = recipes_food_10
    recipes_ingredient_10.amount = Decimal('4.00')
    recipes_ingredient_10.unit = 'dl'
    recipes_ingredient_10 = importer.save_or_locate(recipes_ingredient_10)

    recipes_ingredient_11 = Ingredient()
    recipes_ingredient_11.food = recipes_food_11
    recipes_ingredient_11.amount = Decimal('3.00')
    recipes_ingredient_11.unit = 'pcs'
    recipes_ingredient_11 = importer.save_or_locate(recipes_ingredient_11)

    recipes_ingredient_12 = Ingredient()
    recipes_ingredient_12.food = recipes_food_12
    recipes_ingredient_12.amount = Decimal('0.00')
    recipes_ingredient_12.unit = 'tbsp'
    recipes_ingredient_12 = importer.save_or_locate(recipes_ingredient_12)

    # Processing model: project.recipes.models.Recipe

    from project.recipes.models import Recipe

    recipes_recipe_1 = Recipe()
    recipes_recipe_1.name = 'Pasta al limone'
    recipes_recipe_1.description = 'Lemon pasta, or pasta limone, is a simple pasta dish with a clear taste of fresh lemon. This popular pasta dish can be made both with and without cream, and here you have the cream variant - creamy and fresh! You can make this dish with dried pasta, but if you are going to put an extra tip on it, you make it with homemade pasta. Served alone as a light lunch or as an accompaniment to chicken or white fish.'
    recipes_recipe_1.rating = 4
    recipes_recipe_1.prep_time = 20
    recipes_recipe_1.instruction = '1. Put garlic, lemon peel and pepper together with oil in a pan. Cook over medium heat until the onion is shiny. Add cream and stir in butter. Let the cream sauce simmer on low to medium heat while you cook the pasta.\r\n\r\n2. Boil a large pot of water and add salt. Put the pasta in the boiling water. If you use dried pasta, you can cook it until there are 1-2 minutes left of the cooking time, and if you use fresh pasta, you only need to cook it for 30 seconds - 1 minute. The pasta should not be completely finished, as it should also soak in the sauce.\r\n\r\n3. Turn the pasta into the sauce, and take care of the pasta water. Add lemon juice. Feel free to start with half the amount of lemon juice and add little by little, until you think it is sour enough.\r\n\r\n4. Turn in the parmesan and parsley, and let the pasta soak in the sauce until the pasta is cooked through. Dilute with a little pasta water while the pasta soaks. The pasta water helps to thin out the consistency of the sauce and add a delicious taste. Turn in the parmesan and parsley, and let the pasta soak in the sauce until the pasta is cooked through. Dilute with a little pasta water while the pasta soaks. The pasta water helps to thin out the consistency of the sauce and add a delicious taste.'
    recipes_recipe_1.servings = 4
    recipes_recipe_1.image = 'recipes/Pasta_al_limone.jpg'
    recipes_recipe_1.link = 'https://www.matprat.no/oppskrifter/kos/pasta-al-limone/'
    recipes_recipe_1.data_created = dateutil.parser.parse("2021-04-23T23:16:37.213312+00:00")
    recipes_recipe_1 = importer.save_or_locate(recipes_recipe_1)

    recipes_recipe_1.ingredients.add(recipes_ingredient_1)
    recipes_recipe_1.ingredients.add(recipes_ingredient_2)
    recipes_recipe_1.ingredients.add(recipes_ingredient_3)
    recipes_recipe_1.ingredients.add(recipes_ingredient_4)
    recipes_recipe_1.ingredients.add(recipes_ingredient_5)
    recipes_recipe_1.ingredients.add(recipes_ingredient_6)
    recipes_recipe_1.ingredients.add(recipes_ingredient_7)

    recipes_recipe_2 = Recipe()
    recipes_recipe_2.name = 'Waffles'
    recipes_recipe_2.description = 'Waffles, a success for both young and old. Set out jams, sour cream, butter, sugar and brown cheese, then you are guaranteed that everyone will have their wishes fulfilled. Try our delicious waffle recipe!'
    recipes_recipe_2.rating = 3
    recipes_recipe_2.prep_time = 40
    recipes_recipe_2.instruction = '1. Put everything dry in a bowl and dilute with a little of the milk at a time. Stir well between each time to get a smooth mixture without lumps of milk.\r\n\r\n2. Stir in the eggs and add the melted butter. Let the batter swell for 1/2 hour. Adjust the batter with a little water or milk if it is too thick.\r\n\r\n3. Bake the waffles and serve them hot'
    recipes_recipe_2.servings = 1
    recipes_recipe_2.image = 'recipes/Waffles.jpeg'
    recipes_recipe_2.link = 'https://www.matprat.no/oppskrifter/tradisjon/vafler/'
    recipes_recipe_2.data_created = dateutil.parser.parse("2021-04-23T23:23:28.454837+00:00")
    recipes_recipe_2 = importer.save_or_locate(recipes_recipe_2)

    recipes_recipe_2.ingredients.add(recipes_ingredient_8)
    recipes_recipe_2.ingredients.add(recipes_ingredient_9)
    recipes_recipe_2.ingredients.add(recipes_ingredient_10)
    recipes_recipe_2.ingredients.add(recipes_ingredient_11)

