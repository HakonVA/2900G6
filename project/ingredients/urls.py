from django.urls import include, path

# from .views import (
#     ingredient_index_view,
#     ingredient_deleteAll_view,
#     IngredientListView,
# )

from .views import (
    user_food_list_view,
    # IngredientCreateView,
    # IngredientDeleteView,

    ingredient_deleteAll_view,
)

urlpatterns = [
    path('', view=user_food_list_view, name='ingredients-list'),

    # path('', view=ingredient_index_view, name='ingredients-home'),
    path('deleteAll', ingredient_deleteAll_view, name='deleteAll'),
]