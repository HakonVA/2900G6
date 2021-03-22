from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Food, Pantry
from .forms import PantryForm

from django.contrib import messages

from django.views.generic import (
    View,
    ListView,
    CreateView,
    DeleteView,
)

class PantryIndexView(LoginRequiredMixin, View):
    model = Pantry
    login_url = 'login'
    http_method_names = ['get', 'post', 'delete']
    success_url = 'pantry-home'
    
    
    template_name = "pages/ingredients.html"
    context = None
    # context_object_name = None
    # queryset = None

    @property
    def get_user_queryset(self):
        """ Get the pantry queryset for the current user that is logged into website.
        """
        try:
            queryset = Pantry.objects.filter(user=self.request.user)
        except Pantry.DoesNotExist():
            print("The requested model field does not exist")
        return queryset

    def addItem_is_valid(self, request, fd_name):
        queryset = Food.objects.filter(scientific_name=fd_name)

        # Check if queryset is empty; queyrset is not found in the food database.
        if queryset.count() == 0:
            messages.warning(request, '{} is not present in our food database!'.format(fd_name.capitalize()))
            return 0
    
        # Check for duplicates entries into users pantry list
        pantry_list = [obj.name for obj in self.get_user_queryset]
        if fd_name in pantry_list:
            messages.warning(request, '{} is present in your pantry!'.format(fd_name.capitalize()))
            return 0

        messages.success(request, 'Your pantry was updated successfully!')
        return 1
         
    def get(self, request, *args, **kwargs):

        queryset = self.get_user_queryset
        self.context = {
            'food_list': queryset,
        }
        
        return render(request, template_name=self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):

        form = PantryForm(request.POST or None)
        if "add-item" in request.POST:
            if form.is_valid():  
                fd_name = form.cleaned_data.get("name").lower()

                if self.addItem_is_valid(request, fd_name):
                    model_instance = form.save(commit=False)
                    model_instance.user = self.request.user
                    model_instance.name = fd_name
                    model_instance.save()
                    return redirect(self.success_url)

        if "delete-item" in request.POST:
            if form.is_valid():
                py_id = form.cleaned_data.get("name")
                queryset = self.get_user_queryset
                queryset.filter(py_id=py_id).delete()
                messages.success(request, 'Pantry item was deleted successfully!')
                return redirect(self.success_url)
       
        # Should have an redirect to unsuccessful url???
        return redirect(self.success_url)

pantry_index_view = PantryIndexView.as_view()

class PantryListView(LoginRequiredMixin, ListView):
    model = Pantry
    login_url = 'login'
    template_name = "ingredients/pantry_list_detail.html"
    context_object_name = "food_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

pantry_list_view = PantryListView.as_view()

class PantryCreateView(LoginRequiredMixin, CreateView):
    model = Pantry
    login_url = 'login'
    template_name = "pages/ingredients.html"
    success_url = "/ingredients/"
    form_class = PantryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PantryCreateView, self).form_valid(form)

pantry_create_view = PantryCreateView.as_view()

class PantryDeleteView(LoginRequiredMixin, DeleteView):
    pass

pantry_create_view = PantryDeleteView.as_view()

def pantry_DeleteAll_view(request):
    try:
        Pantry.objects.filter(user=request.user).delete()
    except:
        print("Error: ingredient_deleteAll_view")
    return redirect("pantry-home")