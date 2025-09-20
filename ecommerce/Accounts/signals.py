from django.contrib.auth.models import User
from store.models import ProfileUser
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)
