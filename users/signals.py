from django.dispatch import receiver

from users.models import Curator, Student, User


@receiver.post_save(sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "S":
            Student.objects.create(user=instance)
        elif instance.user_type == "C":
            Curator.objects.create(user=instance)
