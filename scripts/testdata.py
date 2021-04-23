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
    recipes_food_1.name = 'oil'
    recipes_food_1 = importer.save_or_locate(recipes_food_1)

    recipes_food_2 = Food()
    recipes_food_2.name = 'mushrooms'
    recipes_food_2 = importer.save_or_locate(recipes_food_2)

    recipes_food_3 = Food()
    recipes_food_3.name = 'lettuce'
    recipes_food_3 = importer.save_or_locate(recipes_food_3)

    recipes_food_4 = Food()
    recipes_food_4.name = 'butter'
    recipes_food_4 = importer.save_or_locate(recipes_food_4)

    recipes_food_5 = Food()
    recipes_food_5.name = 'shrimps'
    recipes_food_5 = importer.save_or_locate(recipes_food_5)

    recipes_food_6 = Food()
    recipes_food_6.name = 'onions'
    recipes_food_6 = importer.save_or_locate(recipes_food_6)

    # Processing model: project.recipes.models.Ingredient

    from project.recipes.models import Ingredient

    recipes_ingredient_1 = Ingredient()
    recipes_ingredient_1.food = recipes_food_1
    recipes_ingredient_1.amount = Decimal('15.00')
    recipes_ingredient_1.unit = 'ml'
    recipes_ingredient_1 = importer.save_or_locate(recipes_ingredient_1)

    recipes_ingredient_2 = Ingredient()
    recipes_ingredient_2.food = recipes_food_2
    recipes_ingredient_2.amount = Decimal('500.00')
    recipes_ingredient_2.unit = 'g'
    recipes_ingredient_2 = importer.save_or_locate(recipes_ingredient_2)

    recipes_ingredient_3 = Ingredient()
    recipes_ingredient_3.food = recipes_food_3
    recipes_ingredient_3.amount = Decimal('250.00')
    recipes_ingredient_3.unit = 'g'
    recipes_ingredient_3 = importer.save_or_locate(recipes_ingredient_3)

    recipes_ingredient_4 = Ingredient()
    recipes_ingredient_4.food = recipes_food_4
    recipes_ingredient_4.amount = Decimal('45.00')
    recipes_ingredient_4.unit = 'ml'
    recipes_ingredient_4 = importer.save_or_locate(recipes_ingredient_4)

    recipes_ingredient_5 = Ingredient()
    recipes_ingredient_5.food = recipes_food_5
    recipes_ingredient_5.amount = Decimal('500.00')
    recipes_ingredient_5.unit = 'g'
    recipes_ingredient_5 = importer.save_or_locate(recipes_ingredient_5)

    # Processing model: project.recipes.models.Recipe

    from project.recipes.models import Recipe

    recipes_recipe_1 = Recipe()
    recipes_recipe_1.name = 'Taco'
    recipes_recipe_1.description = 'Fiest of taco'
    recipes_recipe_1.rating = 4
    recipes_recipe_1.prep_time = 15
    recipes_recipe_1.instruction = 'Heat the oil in a large pan over medium-high heat and fry the garlic until softened (take care not to let it burn). Add the spices, mushrooms and tomatoes, stir well and cook for another 6–8 minutes or until golden.'
    recipes_recipe_1.servings = 1
    recipes_recipe_1.image = 'recipes/taco.jpg'
    recipes_recipe_1.link = 'https://www.food24.com/recipe/taco-fiesta/?paged=search'
    recipes_recipe_1.data_created = dateutil.parser.parse("2021-04-21T10:18:31.070592+00:00")
    recipes_recipe_1 = importer.save_or_locate(recipes_recipe_1)

    recipes_recipe_1.ingredients.add(recipes_ingredient_1)
    recipes_recipe_1.ingredients.add(recipes_ingredient_2)

    recipes_recipe_2 = Recipe()
    recipes_recipe_2.name = 'Pasta'
    recipes_recipe_2.description = 'pasta dec'
    recipes_recipe_2.rating = 5
    recipes_recipe_2.prep_time = 10
    recipes_recipe_2.instruction = 'Cook the pasta in salted water according to the package instructions. Set aside.'
    recipes_recipe_2.servings = 1
    recipes_recipe_2.image = 'recipes/pasta.jpg'
    recipes_recipe_2.link = 'https://www.food24.com/recipe/creamy-shrimp-pasta-alfredo/?paged=searchhttps://www.food24.com/recipe/creamy-shrimp-pasta-alfredo/?paged=search'
    recipes_recipe_2.data_created = dateutil.parser.parse("2021-04-21T10:22:44.851639+00:00")
    recipes_recipe_2 = importer.save_or_locate(recipes_recipe_2)

    recipes_recipe_2.ingredients.add(recipes_ingredient_4)
    recipes_recipe_2.ingredients.add(recipes_ingredient_5)

