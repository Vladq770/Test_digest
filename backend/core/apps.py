from django.apps import AppConfig
from django.db.models.signals import post_save
from .signals import update_likes


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        Like = self.get_model('Like')
        post_save.connect(update_likes, sender=Like)
    