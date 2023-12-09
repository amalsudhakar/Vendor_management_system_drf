from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# View vendors api/vendors/.


class VendorsList(APIView):
    @swagger_auto_schema(
        responses={200: VendorSerializer(many=True)},
    )
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VendorCreate(APIView):
    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={201: VendorSerializer(),
                   400: "Bad Request",},
    )
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VendorDetails(APIView):
    @swagger_auto_schema(
        responses={200: VendorSerializer},
    )
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(id=vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class VendorUpdate(APIView):
    @swagger_auto_schema(
        request_body=VendorSerializer(),
        responses={
            200: VendorSerializer(),
            400: "Bad Request",
            404: "Vendor Not Found"
        },
    )
    def post(self, request, vendor_id):
        try:
            vendor =  Vendor.objects.get(id=vendor_id)
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        

class VendorDelete(APIView):
    @swagger_auto_schema(
        responses={204: "Vendor deleted",
                   404: "Vendor not found"},
    )
    def delete(self, request, vendor_id):
        try:
            vendor =  Vendor.objects.get(id=vendor_id)
            vendor.delete()
            return Response({'message': 'Vendor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)