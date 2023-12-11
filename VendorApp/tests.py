from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
# Replace 'your_app' with the appropriate app name
from .models import HistoricalPerformance, PurchaseOrder, Vendor
from .serializers import VendorSerializer  # Import your serializer
from rest_framework_simplejwt.tokens import AccessToken


class VendorCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_vendor_create(self):
        # Replace 'vendor-create' with your actual URL name
        url = reverse('create-vendor')
        data = {
            'name': 'Test Vendor',
            'contact_details': 'Contact Info',
            'address': 'Vendor Address',
            'vendor_code': 'V123'
            # Add other required fields based on your Vendor model
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_access(self):
        self.client.credentials()  # Remove authentication token
        # Replace 'vendor-create' with your actual URL name
        url = reverse('create-vendor')
        data = {
            'name': 'Test Vendor',
            'contact_details': 'Contact Info',
            'address': 'Vendor Address',
            'vendor_code': 'V123'
            # Add other required fields based on your Vendor model
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class VendorDetailsUpdateAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Info',
            address='Vendor Address',
            vendor_code='V123'

        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_vendor_details_retrieve(self):
        url = reverse('vendor-details', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vendor_details_update(self):
        url = reverse('vendor-details', kwargs={'pk': self.vendor.pk})
        data = {
            'name': 'Updated Vendor Name',
            'contact_details': 'Updated Contact Info',
            'address': 'Updated Vendor Address',
            'vendor_code': 'V456'

        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, 'Updated Vendor Name')

    def test_vendor_details_destroy(self):
        url = reverse('vendor-details', kwargs={'pk': self.vendor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Vendor.DoesNotExist):
            Vendor.objects.get(pk=self.vendor.pk)


class PurchaseOrderCreateListAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Info',
            address='Vendor Address',
            vendor_code='V123'

        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_purchase_order_create(self):
        url = reverse('purchase-order')
        data = {
            'po_number': 'PO123',
            'vendor': self.vendor.pk,
            'delivery_date': timezone.now() + timezone.timedelta(days=14),
            'items': '{"name":"mobile"}',
            'quantity': '1',
            'status': 'pending',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_purchase_order_list_filter(self):
        url = reverse('purchase-order')
        response = self.client.get(url, {'vendor': self.vendor.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PurchaseOrderDetailsUpdateAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Info',
            address='Vendor Address',
            vendor_code='V123'
        )

        self.purchase_order = PurchaseOrder.objects.create(
            po_number='PO123',
            vendor=self.vendor,
            delivery_date=timezone.now() + timezone.timedelta(days=14),
            items={"name": "mobile"},
            quantity=1,
            status='pending',
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_purchase_order_retrieve(self):
        url = reverse('purchase-order-details',
                      kwargs={'pk': self.purchase_order.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_order_update(self):
        url = reverse('purchase-order-details',
                      kwargs={'pk': self.purchase_order.pk})
        data = {
            'po_number': 'PO456',
            'vendor': self.vendor.pk,
            'delivery_date': timezone.now() + timezone.timedelta(days=14),
            'items': '{"name":"laptop"}',
            'quantity': '1',
            'status': 'pending',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertEqual(self.purchase_order.po_number, 'PO456')
        # Add assertions for other fields being updated

    def test_purchase_order_destroy(self):
        url = reverse('purchase-order-details',
                      kwargs={'pk': self.purchase_order.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(PurchaseOrder.DoesNotExist):
            PurchaseOrder.objects.get(pk=self.purchase_order.pk)


class PerformanceListAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Info',
            address='Vendor Address',
            vendor_code='V123'
        )

        HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.85,
            quality_rating_avg=4.5,
            average_response_time=24.5,
            fulfillment_rate=0.92
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_performance_list_retrieve(self):
        url = reverse('performance-list', kwargs={'vendor_id': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class VendorPerformanceAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Info',
            address='Vendor Address',
            vendor_code='V123'
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_vendor_performance_retrieve(self):
        url = reverse('vendor-performance', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)


class AcknowledgePurchaseOrderAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = AccessToken.for_user(self.user)
        self.api_authentication()

        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Info',
            address='Vendor Address',
            vendor_code='V123'
        )

        self.purchase_order = PurchaseOrder.objects.create(
            po_number='PO123',
            vendor=self.vendor,
            delivery_date=timezone.now() + timezone.timedelta(days=14),
            items={"name": "mobile"},
            quantity=1,
            status='pending',
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_acknowledge_purchase_order(self):
        url = reverse('acknowledge-purchase-order',
                      kwargs={'pk': self.purchase_order.pk})
        data = {
            "acknowledgment_date": "2023-12-10T00:00:00Z"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_purchase_order = PurchaseOrder.objects.get(
            pk=self.purchase_order.pk)

        print("Acknowledgment Date:", updated_purchase_order.acknowledgment_date)
        self.assertIsNotNone(updated_purchase_order.acknowledgment_date)
