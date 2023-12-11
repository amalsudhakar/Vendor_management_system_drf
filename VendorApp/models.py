from django.db.models import Avg
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def calculate_on_time_delivery_rate(self):
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self, status='completed')
        on_time_orders = completed_orders.filter(
            delivery_date__lte=models.F('delivery_date'))
        return on_time_orders.count() / completed_orders.count() if completed_orders.count() > 0 else 0

    def calculate_quality_rating_average(self):
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self, status='completed')
        rated_orders = completed_orders.exclude(quality_rating__isnull=True)
        avg_rating = rated_orders.aggregate(
            avg_rating=Avg('quality_rating'))['avg_rating']
        return avg_rating if avg_rating is not None else 0

    def calculate_average_response_time(self):
        acknowledged_orders = PurchaseOrder.objects.filter(
            vendor=self, acknowledgment_date__isnull=False)
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds()
                          for order in acknowledged_orders]
        return sum(response_times) / len(response_times) if response_times else 0

    def calculate_fulfillment_rate(vendor):
        completed_orders = vendor.purchaseorder_set.filter(status='completed')
        successful_orders = completed_orders.exclude(
            status='completed', quality_rating__isnull=True)
        total_orders = vendor.purchaseorder_set.all()

        print(completed_orders.count())
        print(successful_orders.count())
        print(total_orders.count())
        print(successful_orders.count() / total_orders.count())
        return successful_orders.count() / total_orders.count() if total_orders.count() > 0 else 0

    def save(self, *args, **kwargs):
        self.on_time_delivery_rate = self.calculate_on_time_delivery_rate()
        print(self.calculate_on_time_delivery_rate())
        print(self.calculate_quality_rating_average())
        print(self.calculate_average_response_time())
        self.quality_rating_avg = self.calculate_quality_rating_average()
        self.average_response_time = self.calculate_average_response_time()
        self.fulfillment_rate = self.calculate_fulfillment_rate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.po_number}: {self.vendor.name}"

    def clean(self):
        if self.delivery_date < timezone.now():
            raise ValidationError("Delivery date cannot be in the past.")


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"Historical Performance for {self.vendor.name} on {self.date}"
