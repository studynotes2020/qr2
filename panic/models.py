from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

import datetime, time
from django.http import StreamingHttpResponse

panic_status = [("normal", "Normal"), ("panic", "Panic")]


class Panic(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=250, choices=panic_status, default="normal")



@receiver(pre_save, sender=Panic)
def print_email(sender, instance, **kwargs):
    print(f"{instance.user} -> {instance.status}")
