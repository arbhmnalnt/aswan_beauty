from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from product.models import *


class ProductDetailView(DetailView):
    model = Product
    template_name = 'website/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'

class productsListView(ListView):
    model           = Product
    template_name   = "website/product_list.html"
    # will 
    context_object_name =   "products"