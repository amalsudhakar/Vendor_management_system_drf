from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer
from drf_yasg.utils import swagger_auto_schema

from django_filters import rest_framework as django_drf_filters
import django_filters

# View vendors api/vendors/.


class VendorCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class =VendorSerializer


class PurchaseOrderCreateList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
            

class PurchaseOrderDetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PerformanceList(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformance


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