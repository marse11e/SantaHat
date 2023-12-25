from django.db.models.signals import post_save
from django.dispatch import receiver

from mainapp.models import PhotoEdit
from mainapp.photo_edit import PhotoEditService

@receiver(post_save, sender=PhotoEdit)
def update_photo(sender, instance, created, **kwargs):
    if created:
        service = PhotoEditService(instance.image.path)
        service.photo_edit()