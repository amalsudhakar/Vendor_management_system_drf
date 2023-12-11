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
    cd Vendor_management_system_drf
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

    - POST /api/vendors/: Create a new vendor.
    - GET /api/vendors/: List all vendors.
    - GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
    - PUT /api/vendors/{vendor_id}/: Update a vendor's details.
    - DELETE /api/vendors/{vendor_id}/: Delete a vendor.
    - POST /api/purchase_orders/: Create a purchase order.
    - GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
    - GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    - PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    - DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
    - GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.
    - POST /api/token/: Generates a token with valid user credentials for API access.
    - POST /api/token/refresh/: Renews the token for continued API access without re-authentication.

7. Authentication

    JWT Authentication is required for all the endpoints.
    Obtain a JWT token by sending a POST request to /api/token/ with valid credentials.
    Include the token in the Authorization header for authenticated endpoints (Authorization: Bearer <token>).