from django.db.models.signals import post_save
from django.dispatch import receiver

from reports.models import Report
from reports.tasks import create_report


@receiver(post_save, sender=Report)
def report_post_save(sender, instance, created, **kwargs):
    if created:
        create_report.delay(instance.id)
