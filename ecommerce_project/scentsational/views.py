from django.shortcuts import render

# Create your views here.
# scentsational/views.py

from django.shortcuts import render
from .models import Customer  # Import the Customer model

# Define a view to list all customers
def customer_list(request):
    # Fetch all customers from the database
    customers = Customer.objects.all()
    # Render the 'customer_list.html' template and pass the customers data
    return render(request, 'customers/customer_list.html', {'customers': customers})
