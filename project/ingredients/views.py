from django.shortcuts import render

from .models import Food

def get_ingredients(request):
    object_list = Food.objects.all()
    
    context = {
        'object_list': object_list,
    }

    return render(request, 'ingredients/ingredients-home.html', context)