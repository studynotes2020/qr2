from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Visit
from django.urls import reverse_lazy
from django import forms
from .forms import VisitForm


class VisitListView(ListView):
    model = Visit
    template_name = "home.html"


class VisitDetailView(DetailView):
    model = Visit
    template_name = "visit_detail.html"


class VisitCreateView(CreateView):
    model = Visit
    form_class = VisitForm
    template_name = "visit_new.html"
    # fields = ["name", "car_plate", "visit_at"]


class VisitUpdateView(UpdateView):
    model = Visit
    form_class = VisitForm
    template_name = "visit_edit.html"
    # fields = "__all__"
    # fields = ["name", "car_plate", "visit_at"]


class VisitDeleteView(DeleteView):
    model = Visit
    template_name = "visit_delete.html"
    success_url = reverse_lazy("visit:home")
