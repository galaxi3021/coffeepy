from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

from .models import Product, Recipe

class IndexView(generic.ListView):
    model = Product
    template_name = "products/index.html"


class DetailView(generic.DetailView):
    model = Product
    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["ingredients"] = Recipe.objects.filter(product=self.object)
        return context

class IngredientInLine(InlineFormSetFactory):
    model = Recipe
    fields = '__all__'

class UpdateProductView(UpdateWithInlinesView):
    model = Product
    inlines = [IngredientInLine]
    fields = ['image','product_type','name', 'description', 'price']
    template_name = 'products/form.html'

class CreateProductView(CreateWithInlinesView):
    model = Product
    inlines = [IngredientInLine]
    fields = ['image','product_type','name', 'description', 'price']
    template_name = 'products/form.html'

class DeleteProductView(generic.DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')

