from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import AcknowledgePurchaseOrderSerializer, VendorPerformanceSerializer, VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as django_drf_filters
import django_filters
# View vendors api/vendors/.


class VendorCreate(generics.ListCreateAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderCreateList(generics.ListCreateAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PerformanceList(generics.ListAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    serializer_class = HistoricalPerformanceSerializer

    def get_queryset(self):
        vendor_id = self.kwargs['pk']
        return HistoricalPerformance.objects.filter(vendor_id=vendor_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "Details not found for this vendor ID."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class VendorPerformance(generics.RetrieveAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    serializer_class = VendorPerformanceSerializer

    def get_queryset(self):
        return Vendor.objects.all()

    def get(self, request, *args, **kwargs):
        vendor = self.get_object()
        serializer = self.get_serializer(vendor)
        return Response(serializer.data)


class AcknowledgePurchaseOrder(generics.UpdateAPIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]
    serializer_class = AcknowledgePurchaseOrderSerializer

    def get_queryset(self):
        return PurchaseOrder.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.vendor.calculate_average_response_time()
        instance.vendor.save()

# class CustomPlanTypeFilter(django_filters.CharFilter):
#     def filter(self, queryset, value):

#         if value.lower() == 'none':
#             return queryset.filter(plan_type=None)
#         return super().filter(queryset, value)


# class ContactsFilter(django_drf_filters.FilterSet):
#     pos = django_drf_filters.CharFilter(
#         field_name="position_applying_for", lookup_expr="exact"
#     )
#     stage = django_drf_filters.CharFilter(
#         field_name="pipeline_stage__stage_name", lookup_expr="exact"
#     )
#     plan_type = CustomPlanTypeFilter()

#     email = django_drf_filters.CharFilter(field_name="client_email", lookup_expr="exact")

#     class Meta:
#         model = Vendor
#         fields = ["availability"]

# class ContactsView(AutoPrefetchViewSetMixin, generics.ListAPIView):
#     def get(self, request, *args, **kwargs):
#             return super().get(request, *args, **kwargs)

#     queryset = Contacts.objects.all()
#     serializer_class = ContactsSerializer
#     filter_backends = [
#     filters.SearchFilter,
#     filters.OrderingFilter,
#     django_drf_filters.DjangoFilterBackend,
#     ]
#     pagination_class = ContactsPagination
#     search_fields = ["name"]
#     ordering_fields = ["name", "created_at"]
#     ordering = ["-created_at"]
#     filterset_class = ContactsFilt
