from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import AcknowledgePurchaseOrderSerializer, VendorPerformanceSerializer, VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class VendorCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderCreateList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vendor']
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PerformanceList(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer


class AcknowledgePurchaseOrder(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AcknowledgePurchaseOrderSerializer

    def get_queryset(self):
        return PurchaseOrder.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.vendor.calculate_average_response_time()
        instance.vendor.save()
