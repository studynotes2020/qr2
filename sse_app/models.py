from django.db import models


class Notification(models.Model):
    text = models.CharField(max_length=200)
    sent = models.BooleanField(default=True)

    def __str__(self):
        return self.text
