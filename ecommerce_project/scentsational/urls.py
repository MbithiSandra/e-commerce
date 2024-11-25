# scentsational/urls.py

from django.urls import path
from . import views  # Import the views from your app

urlpatterns = [
    # Define a URL pattern for the customer list view
    path('customers/', views.customer_list, name='customer_list'),
]
