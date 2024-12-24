# E-commerce API  


## Project Overview
This is a backend API designed for managing products in an e-commerce platform, built using Django and Django REST Framework. The API supports CRUD operations for products, user authentication, and allows users to search and filter products based on category, price range, and stock availability.

## Features
User Management (CRUD): Allows users to create, view, update, and delete products. Only authenticated users can perform CRUD operations.
Product Management (CRUD): Manage products with attributes like name, description, price, stock quantity, and category.
Product Search: Search for products by name or category. Supports partial matching for flexible search.
Product View: View a list of products or individual product details by ID, with optional filtering by category, price range, and stock availability.
Pagination: Pagination for product listing and search results to handle large datasets efficiently.
Authentication: User authentication using Django's built-in system. Token-based authentication (JWT) is also supported.
Filtering: Filter products by category, price range, and stock availability.
## Technologies Used
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django REST Framework (DRF): A powerful toolkit for building Web APIs.
Django Filter: A library for simplifying filtering in Django REST Framework.
JWT Authentication: JSON Web Token (JWT) for securing the API and handling authentication.
## Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/fatachyoussef9/ecommerce_api.git









Example Postman request for adding a product (POST):
{
    "name": "Laptop",
    "description": "High-end laptop",
    "price": 1200.50,
    "category": 1
}
