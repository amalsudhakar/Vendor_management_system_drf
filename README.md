# Vendor Management System using Django Rest Framework

The Vendor Management System is a web application built with Django Rest Framework (DRF) to efficiently manage vendors and purchase orders.

## Introduction

This system offers RESTful APIs to perform various operations related to vendors and purchase orders. It includes functionalities such as creating, updating, retrieving, and deleting vendor details along with managing purchase orders. The project utilizes Simple JWT for token-based authentication and includes Swagger and ReDoc for API documentation.

## Features
- Vendor Management: Create, retrieve, update, and delete vendor details.
- Purchase Order Handling: Manage purchase orders - create, update, retrieve, and delete.
- Token Authentication: Secure API access using Simple JWT for token-based authentication.
- API Documentation: Swagger and ReDoc integration for comprehensive API documentation.

## Prerequisites

Make sure you have the following installed before running the application:

- Python (3.x recommended)
- Django
- Django Rest Framework
- Virtual environment 

## Installation

1. Clone the Repository
    ```sh
    git clone https://github.com/amalsudhakar/Vendor_management_system_drf.git
    cd Vendor_management_system_drf
    ```

2. Create and Activate a Virtual Environment (Optional but Recommended):
    ```sh
    python -m venv venv
    ```
3. Install Dependencies
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
6. Testing the API:
    - Run tests to ensure API functionality:
    ```sh
    python manage.py test
    ```

## Api Endpoints:
    
**VendorApp URLs:** Includes URLs from the VendorApp application.

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

**Token Authentication URLs:** Endpoints for token-based authentication using Simple JWT.

    - /api/token/: Endpoint to obtain a token.
    - /api/token/refresh/: Endpoint to refresh an existing token.

**Admin URLs:** Routes requests to Django's admin interface.

    - Accessible at /admin/.

**Swagger Documentation URLs:** Endpoint URLs for API documentation using Swagger and ReDoc.

    - /swagger<str:format>: Provides JSON format of the API schema.
    - /swagger/: UI for Swagger documentation.
    - /redoc/: UI for ReDoc documentation.

## Authentication

    JWT Authentication is required for all the endpoints.
    Obtain a JWT token by sending a POST request to /api/token/ with valid credentials.
    Include the token in the Authorization header for authenticated endpoints (Authorization: Bearer <token>).