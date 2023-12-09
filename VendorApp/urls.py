from django.urls import path
from .views import VendorsList, VendorCreate

urlpatterns = [
    path('vendors/', VendorCreate.as_view(), name='create-vendor'),
    path('vendors/list/', VendorsList.as_view(), name='vendor-list'),
]