# Vendor Management System using Django Rest Framework

The Vendor Management System is a web application built with Django Rest Framework (DRF) to efficiently manage vendors and purchase orders.

## Introduction

This system offers RESTful APIs to perform various operations related to vendors and purchase orders. It includes functionalities such as creating, updating, retrieving, and deleting vendor details along with managing purchase orders. The project utilizes Simple JWT for token-based authentication and includes Swagger and ReDoc for API documentation.

## Features
- Vendor Management: Create, retrieve, update, and delete vendor details.
- Purchase Order Handling: Manage purchase orders - create, update, retrieve, and delete.
- Vendor Performance Evaluation: Manage and track vendor performance metrics.
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
    venv\Scripts\activate
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

### VendorApp URLs:

This section outlines the various endpoints available for interacting with the VendorApp, which manages vendors and purchase orders. The following URLs provide access to functionalities related to vendor management, purchase order handling, and performance metrics calculations within the Vendor Management System.

1. **POST /api/vendors/: Create a new vendor.**
   - Endpoint for creating a new vendor by providing details such as name, contact details, address, and a unique vendor code. Utilizes the `Vendor` model to create a new entry in the database.

2. **GET /api/vendors/: List all vendors.**
   - Retrieves a list of all vendors available in the system. Fetches data from the `Vendor` model and returns a collection of vendor details.

3. **GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.**
   - Retrieves the details of a specific vendor identified by `{vendor_id}`. Fetches data from the `Vendor` model based on the unique identifier and returns the specific vendor's information.

4. **PUT /api/vendors/{vendor_id}/: Update a vendor's details.**
   - Updates the details of a specific vendor identified by `{vendor_id}`. Utilizes the `Vendor` model to modify the existing vendor's information.

5. **DELETE /api/vendors/{vendor_id}/: Delete a vendor.**
   - Deletes a specific vendor identified by `{vendor_id}`. Removes the vendor entry from the system using the `Vendor` model.

6. **POST /api/purchase_orders/: Create a purchase order.**
   - Creates a new purchase order by providing details such as purchase order number, vendor reference, order date, delivery date, items, quantity, and status. Uses the `PurchaseOrder` model to create a new purchase order entry in the database.

7. **GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.**
   - Retrieves a list of all purchase orders available in the system. Additionally, it offers an option to filter purchase orders by a specific vendor. Fetches data from the `PurchaseOrder` model and returns relevant purchase order details.

8. **GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.**
   - Retrieves the details of a specific purchase order identified by `{po_id}`. Fetches data from the `PurchaseOrder` model based on the unique identifier and returns the specific purchase order's information.

9. **PUT /api/purchase_orders/{po_id}/: Update a purchase order.**
   - Updates the details of a specific purchase order identified by `{po_id}`. Utilizes the `PurchaseOrder` model to modify the existing purchase order's information.

10. **DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.**
    - Deletes a specific purchase order identified by `{po_id}`. Removes the purchase order entry from the system using the `PurchaseOrder` model.

11. **GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.**
    - Retrieves the performance metrics of a specific vendor identified by `{vendor_id}`. Utilizes the `Vendor` model's methods (`calculate_on_time_delivery_rate`, `calculate_quality_rating_average`, `calculate_average_response_time`, `calculate_fulfillment_rate`) to calculate and return the vendor's performance metrics.


### Token Authentication URLs:

Endpoints for token-based authentication using Simple JWT.

- **/api/token/:** 
  - Endpoint to obtain a token for API access using valid user credentials such as username and password.

- **/api/token/refresh/:** 
  - Endpoint to refresh an existing token, allowing continued API access without re-authentication.

### Admin URLs:

Routes requests to Django's admin interface.

- **/admin/:**
  - Provides access to Django's built-in admin panel for managing system entities and configurations.

### Swagger Documentation URLs:

Endpoint URLs for API documentation using Swagger and ReDoc.

- **/swaggerstr:format:** 
  - Provides the API schema in JSON format.

- **/swagger/:** 
  - UI for Swagger documentation, offering interactive API documentation and testing.

- **/redoc/:** 
  - UI for ReDoc documentation, providing a clean and organized view of the API documentation.


## Authentication

JWT Authentication is required for accessing all the endpoints within the Vendor Management System.

### Obtaining a JWT Token:

1. **Use Superuser Credentials:**
   - Utilize the username and password of the superuser created during the setup process. If you haven't created a superuser yet, you can do so using the following command:
     ```bash
     python manage.py createsuperuser
     ```
   - Enter the desired username, email, and a secure password for the superuser.

2. **Request a JWT Token:**
   - Send a POST request to the `/api/token/` endpoint with the superuser's username and password in the request body.
     ```bash
     curl -X POST http://127.0.0.1:8000/api/token/ 
     -H "Content-Type: application/json" 
     -d '{"username": "your_superuser_username", "password": "your_superuser_password"}'
     ```
   - This request will return a JWT token in the response, typically in the format:
     ```json
     {
         "access": "your_access_token",
         "refresh": "your_refresh_token"
     }
     ```

3. **Include Token in Authorization Header:**
   - Once you have obtained the token, include it in the Authorization header as follows:
     ```
     Authorization: Bearer <your_access_token>
     ```
   - Use this Authorization header in subsequent requests to authenticated endpoints, replacing `<your_access_token>` with the actual access token obtained.

By following these steps and using the superuser's username and password, you can obtain a JWT token necessary for accessing the authenticated endpoints within the Vendor Management System. This ensures secure access to the system's functionalities requiring authentication.


## Example Usage:

**Sample Requests:**
Here are cURL examples demonstrating how to interact with the API endpoints:

- **Creating a Vendor:**
  ```bash
  curl -X POST http://your_domain/api/vendors/ 
  -H "Authorization: Bearer <your_access_token>" 
  -H "Content-Type: application/json" 
  -d '{"name": "Vendor Name", "contact_details": "Contact Info", "address": "Vendor Address", "vendor_code": "ABC123"}'
  ```
- **Updating a Purchase Order:**

    ```bash
    curl -X PUT http://your_domain/api/purchase_orders/{po_id}/ 
    -H "Authorization: Bearer <your_access_token>" 
    -H "Content-Type: application/json" 
    -d '{"status": "completed"}'
    ```
- **Retrieving Vendor Performance Metrics:**

    ```bash
    curl -X GET http://your_domain/api/vendors/{vendor_id}/performance 
    -H "Authorization: Bearer <your_access_token>"
    ```
