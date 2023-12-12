from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.utils import timezone


@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    if created or instance.status != "completed":
        return

    vendor = instance.vendor

    # Calculate metrics using Vendor methods
    on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
    quality_rating_avg = vendor.calculate_quality_rating_average()
    average_response_time = vendor.calculate_average_response_time()
    fulfillment_rate = vendor.calculate_fulfillment_rate()

    # Convert decimal values to percentages
    on_time_delivery_rate_percent = round(on_time_delivery_rate * 100, 2)
    quality_rating_avg_percent = round(quality_rating_avg * 100, 2)
    average_response_time_percent = round(average_response_time * 100, 2)
    fulfillment_rate_percent = round(fulfillment_rate * 100, 2)

    # Update Vendor instance with calculated metrics as percentages
    vendor.on_time_delivery_rate = on_time_delivery_rate_percent
    vendor.quality_rating_avg = quality_rating_avg_percent
    vendor.average_response_time = average_response_time_percent
    vendor.fulfillment_rate = fulfillment_rate_percent

    vendor.save()

    details = {"date": timezone.now(),
               "on_time_delivery_rate": on_time_delivery_rate,
               "quality_rating_avg": quality_rating_avg,
               "average_response_time": average_response_time,
               "fulfillment_rate": fulfillment_rate}
    historical_performance = HistoricalPerformance.objects.update_or_create(
        vendor=vendor,
        defaults={**details}
    )
