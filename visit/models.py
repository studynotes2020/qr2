from django.db import models
import hashlib
from django.shortcuts import render, reverse, redirect
from datetime import date


class Visit(models.Model):
    name = models.CharField(max_length=100)
    car_plate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    visit_at = models.DateTimeField("Visit at")
    leave_at = models.DateTimeField("Leave at", null=True)
    hashed = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.hashed = f"{self.id},{self.name},{self.car_plate},{self.visit_at}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("visit:visit_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-id"]
