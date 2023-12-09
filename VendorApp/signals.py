# from django.db.models.signals import post_save, pre_delete
# from django.dispatch import receiver
# from django.db.models import Count, Avg
# from django.utils import timezone
# from .models import Vendor, PurchaseOrder, HistoricalPerformance

# @receiver(post_save, sender=PurchaseOrder)
# def update_vendor_performance_metrics(sender, instance, created, **kwargs):
#     vendor = instance.vendor

#     # Calculate On-Time Delivery Rate
#     if instance.status == 'completed':
#         completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
#         on_time_delivered_pos = completed_pos.filter(delivery_date__lte=timezone.now()).count()
#         on_time_delivery_rate = on_time_delivered_pos / completed_pos.count() if completed_pos.count() > 0 else 0
#         vendor.on_time_delivery_rate = on_time_delivery_rate

#     # Calculate Quality Rating Average
#     if instance.quality_rating is not None:
#         quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, quality_rating__isnull=False).aggregate(avg_rating=Avg('quality_rating'))
#         vendor.quality_rating_avg = quality_rating_avg['avg_rating'] or 0

#     # Calculate Average Response Time
#     if instance.acknowledgment_date is not None:
#         response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).annotate(
#             response_time=timezone.F('acknowledgment_date') - timezone.F('issue_date')
#         ).aggregate(avg_response_time=Avg('response_time'))
#         vendor.average_response_time = response_times['avg_response_time'] or 0

#     # Calculate Fulfilment Rate
#     total_pos = PurchaseOrder.objects.filter(vendor=vendor)
#     fulfilled_pos = total_pos.filter(status='completed')
#     fulfillment_rate = fulfilled_pos.count() / total_pos.count() if total_pos.count() > 0 else 0
#     vendor.fulfillment_rate = fulfillment_rate

#     vendor.save()

# @receiver(post_save, sender=PurchaseOrder)
# def update_historical_performance(sender, instance, created, **kwargs):
#     vendor = instance.vendor

#     # Update Historical Performance
#     historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=vendor)
#     historical_performance.on_time_delivery_rate = vendor.on_time_delivery_rate
#     historical_performance.quality_rating_avg = vendor.quality_rating_avg
#     historical_performance.average_response_time = vendor.average_response_time
#     historical_performance.fulfillment_rate = vendor.fulfillment_rate
#     historical_performance.save()

# @receiver(pre_delete, sender=PurchaseOrder)
# def update_on_delete(sender, instance, **kwargs):
#     # When a PurchaseOrder is deleted, update the related Vendor and HistoricalPerformance
#     update_vendor_performance_metrics(sender, instance, False)
#     update_historical_performance(sender, instance, False)
