from django import forms
from .models import Visit
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from datetime import date
from django.contrib.admin.widgets import AdminSplitDateTime


class VisitForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    car_plate = forms.CharField(max_length=100)
    visit_at = forms.SplitDateTimeField(widget=AdminSplitDateTime)

    class Meta:
        model = Visit
        fields = ["name", "car_plate", "visit_at"]
        # widgets = {
        #     "visit_at": forms.DateInput(attrs={
        #         "type": "date",
        #         "value": str(date.today()),
        #         "min": str(date.today()),
        #     })
        #     # "visit_at": forms.DateInput,
        # }
        help_texts = {
            "car_plate": "Ex: PFQ5217",
            "visit_at": "Format: dd/mm/yyyy",
        }
