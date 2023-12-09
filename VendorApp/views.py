from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
from drf_yasg.utils import swagger_auto_schema

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
        responses={201: VendorSerializer()},
    )
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)