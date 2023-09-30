from django.db import models

# Create your models here.


class Device(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    port = models.IntegerField(default=22)
    system = models.CharField(max_length=200, default="N/A", blank=False, null=False)
    available_space = models.IntegerField(default=-1)
    free_space = models.IntegerField(default=-1)

    def __str__(self):
        return self.hostname
