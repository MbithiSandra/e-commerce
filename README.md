# e-commerce
# E-Commerce Django Models

This project implements an e-commerce system with `Customer` and `Order` models in Django, showcasing one-to-many data relationships.

## Features
- Customers can place multiple orders.
- Orders are associated with a single customer.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/MbithiSandra/e-commerce.git
   cd ecommerce_project
2.Install dependencies:
pip install -r requirements.txt
3. Apply migrations:
python manage.py migrate
4.Create a superuser for admin access:
python manage.py createsuperuser
5. Start the server:
python manage.py runserver
6.Access the admin panel at http://127.0.0.1:8000/admin.
Username: Sandra
Password:123
