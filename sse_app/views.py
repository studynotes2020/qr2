import datetime
import time
from django.http import StreamingHttpResponse, HttpResponse
from .models import Notification
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from panic.models import Panic
from django.shortcuts import render, redirect

def stream(request):
    def event_stream():
        for _ in range(3):
            time.sleep(1)
            notification = Notification.objects.filter(sent=True).first()
            yield '%s %s\n\n' % (notification.text, datetime.datetime.now())

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


# @receiver(pre_save, sender=Panic)
# def print_sender(sender, instance, **kwargs):
#     print(f"{instance.user} -> {instance.status}")
#     print(Notification.objects.filter(sent=True).first())
