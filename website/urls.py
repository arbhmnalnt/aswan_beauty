from django.urls import path
from .views import *

app_name="website"

urlpatterns=[
    path('', productsListView.as_view(), name='products_list'),  

]