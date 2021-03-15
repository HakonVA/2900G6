from django.urls import include, path

from .views import (
    ingredient_index_view,
    ingredient_deleteAll_view,
    IngredientListView,
)

# from .views import (
#     IngredientListView,
#     IngredientCreateView,
#     IngredientDeleteView,
# )


urlpatterns = [
    # path('', view=ingredient_index_view, name='ingredients-home'),
    path('', IngredientListView.as_view(), name='ingredients-home'),
    path('deleteAll', ingredient_deleteAll_view, name='deleteAll'),
]