from django.urls import path
from .views import AcknowledgePurchaseOrder, VendorCreate, VendorDetailsUpdate, PurchaseOrderCreateList, PurchaseOrderDetailsUpdate, PerformanceList, VendorPerformance

urlpatterns = [
    path('vendors/', VendorCreate.as_view(), name='create-vendor'),
    path('vendors/<int:pk>/', VendorDetailsUpdate.as_view(), name='vendor-details'),
    path('vendors/<int:pk>/performance/',
         PerformanceList.as_view(), name='performance-list'),
    path('vendors/<int:pk>/performance/',
         VendorPerformance.as_view(), name='vendor-performance'),

    path('purchase_orders/', PurchaseOrderCreateList.as_view(),
         name='purchase-order'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailsUpdate.as_view(),
         name='purchase-order-details'),
    path('purchase_orders/<int:pk>/acknowledge/',
         AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order'),

]
