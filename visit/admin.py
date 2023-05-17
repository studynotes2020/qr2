from django.contrib import admin
from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car_plate', 'visit_at', 'hashed')


admin.site.register(Visit, VisitAdmin)
