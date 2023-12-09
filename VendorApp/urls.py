from django.urls import path
from .views import VendorsList, VendorCreate, VendorDetails, VendorUpdate, VendorDelete

urlpatterns = [
    path('vendors/', VendorCreate.as_view(), name='create-vendor'),
    path('vendors/list/', VendorsList.as_view(), name='vendor-list'),
    path('vendors/<int:vendor_id>/', VendorDetails.as_view(), name='vendor-details'),
    path('vendors/update/<int:vendor_id>/', VendorUpdate.as_view(), name='vendor-update'),
    path('vendors/delete/<int:vendor_id>/', VendorDelete.as_view(), name='vendor-dekete'),
]