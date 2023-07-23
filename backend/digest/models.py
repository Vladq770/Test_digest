from django.db import models
from django.utils import timezone

from core.models import User, Post, Blog, Subscription


class Digest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user) + str(self.created_at)
