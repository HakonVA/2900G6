from django.shortcuts import render, redirect
from django.http import Http404

from .models import Food
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
    
    form = None
    obj = None

    try:
        obj = Food.objects.all()

        form = FoodCreateForm(request.POST or None)
        if form.is_valid():
            food_name = form.cleaned_data.get("scientific_name")
            Food.objects.create(scientific_name=food_name)

    except obj.DoesNotExist:
        raise Http404

    return render(request, "pages/ingredients.html", {"objects": obj, "form": form})

def ingredient_update_view(request):
    pass

def ingredient_deleteAll_view(request):
    try:
        Food.objects.all().delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect(ingredient_index_view)