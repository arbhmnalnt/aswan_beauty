from django.urls import path
from .views import *

app_name="website"

urlpatterns=[
    path('', productsListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),

]