from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from reclamation.models import Complaint
from counji.models import Counji

@receiver(post_save, sender=Complaint)
def create_complaint_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.user_profile.user, notification_type='complaint')

@receiver(post_save, sender=Counji)
def create_leave_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.user_profile.user_employee.user, notification_type='leave')
