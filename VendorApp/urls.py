from django.urls import path
from .views import  VendorCreate, VendorDetailsUpdate, PurchaseOrderCreateList, PurchaseOrderDetailsUpdate, PerformanceList

urlpatterns = [
    path('vendors/', VendorCreate.as_view(), name='create-vendor'),
    path('vendors/<int:pk>/', VendorDetailsUpdate.as_view(), name='vendor-details'),

    path('purchase_orders/', PurchaseOrderCreateList.as_view(), name='purchase-order'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailsUpdate.as_view(), name='purchase-order-details'),

    path('vendors/<int:pk>/performance/', PerformanceList.as_view(), name='performance-list'),
    
]