from django import forms
from .models import Visit
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from datetime import date


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "car_plate", "visit_at"]
        widgets = {
            # "visit_at": forms.DateInput(attrs={
            #     "type": "date",
            #     "value": str(date.today()),
            #     "min": str(date.today()),
            # })
            "visit_at": forms.DateInput,
        }
        help_texts = {
            "car_plate": "Ex: PFQ5217",
            "visit_at": "Format: mm/dd/yyyy",
        }
