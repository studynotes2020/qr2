from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Visit
from django.urls import reverse_lazy
from django import forms
from .forms import VisitForm
from django.shortcuts import render
from django.views.generic.edit import BaseCreateView, TemplateResponseMixin
from django.views.generic.list import BaseListView
from django.template import RequestContext
from django.views.generic import View


class FormAndListView(View):
    model = Visit
    form_class = VisitForm
    template_name = 'visit_create_list.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        visits = Visit.objects.all()[:5]
        return render(self.request, self.template_name, {"form": form, "visits": visits,})

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                form.save()
                form = VisitForm  # clear the form
                visits = Visit.objects.all()[:5]  # only return 5 objects
                return render(request, self.template_name, {"form": form, "visits": visits,})


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
    success_url = reverse_lazy("visit:visit_create_list")

