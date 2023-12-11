# Vendor Management System

This project is a Django-based Vendor Management System API that enables users to manage vendors, their purchase orders, and track vendor performance.

## Description

This Vendor Management System API provides functionalities to:

- Create, retrieve, update, and delete vendors.
- Manage purchase orders associated with vendors.
- Track historical performance metrics for vendors.

## Prerequisites

Make sure you have the following installed before running the application:

- Python (version 3.11.4)
- Django
- Django Rest Framework


## Installation

1. Clone the Repository
    ```sh
    git clone https://github.com/amalsudhakar/Vendor_management_system_drf.git
    cd project_folder
    ```
2. Install Dependencies
    ```sh
    pip install -r requirements.txt
    ```
3. Database Setup
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Create Superuser (Optional)
    ```sh
    python manage.py createsuperuser
    ```
5. Run the Development Server
    ```sh
    python manage.py runserver
    ```
6. API Endpoints

    - POST /api/v1/vendors/: Create a new vendor.
    - GET /api/v1/vendors/: Retrieve all vendors.
    - GET /api/v1/vendors/<vendor_id>/: Retrieve details of a specific vendor.
    - PUT /api/v1/vendors/<vendor_id>/: Update details of a specific vendor.
    - DELETE /api/v1/vendors/<vendor_id>/: Delete a specific vendor.
    - POST /api/v1/vendors/<vendor_id>/purchase_orders/: Create a purchase order for a vendor.
    - GET /api/v1/vendors/<vendor_id>/purchase_orders/: Retrieve all purchase orders for a vendor.
    - GET /api/v1/vendors/<vendor_id>/performance/: Retrieve historical performance for a vendor.
    - GET /api/v1/vendors/<vendor_id>/vendor_performance/: Retrieve performance details for a vendor.
    - PUT /api/v1/purchase_orders/<order_id>/acknowledge/: Acknowledge a purchase order.

7. Authentication
    JWT Authentication is required for most endpoints.
    Obtain a JWT token by sending a POST request to /api/token/ with valid credentials.
    Include the token in the Authorization header for authenticated endpoints (Authorization: Bearer <token>).