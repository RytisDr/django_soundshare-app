from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from . models import Sound, SoundFile


@receiver(pre_delete, sender=SoundFile, dispatch_uid="delete_sound_file")
def delete_sound_file(sender, instance, **kwargs):
    instance.file.delete()


@receiver(post_delete, sender=Sound, dispatch_uid="delete_sound_file_info")
def delete_sound_file_info(sender, instance, **kwargs):
    soundFilePk = instance.sound_file.pk
    match = SoundFile.objects.get(pk=soundFilePk)
    match.delete()
