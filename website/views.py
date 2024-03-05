from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from product.models import *


# Create your views here.


# Create your views here.
class productsListView(ListView):
    model           = Product
    template_name   = "product/product_list.html"
    # will 
    context_object_name =   "products"