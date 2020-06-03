from django.apps import AppConfig


class SoundsAppConfig(AppConfig):
    name = 'sounds_app'

    def ready(self):
        from .signals import delete_sound_file
