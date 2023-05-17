import datetime
import time
from django.http import StreamingHttpResponse
from .models import Notification


def stream(request):
    def event_stream():
        while True:
            time.sleep(1)
            notification = Notification.objects.filter(sent=True).first()
            yield 'Panic: %s %s\n\n' % (notification.text, datetime.datetime.now())

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
