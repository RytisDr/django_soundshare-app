from django.db import models
from django.utils import timezone
# Create your models here.


class IpAddresses(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    last_visited = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.last_visited = timezone.now()
        return super(IpAddresses, self).save()

    def __str__(self):
        return f"{self.ip_address} - {self.last_visited}"
