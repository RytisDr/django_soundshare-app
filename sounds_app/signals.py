from django.db.models.signals import pre_delete
from django.dispatch import receiver
from . models import Sound, SoundFile


@receiver(pre_delete, sender=SoundFile, dispatch_uid="delete_sound_file")
def delete_sound_file(sender, instance, **kwargs):
    print("**** signal received")
    print(instance)
    print(kwargs)
    instance.file.delete()
    instance.save()
