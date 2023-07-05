from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Visit
from django.urls import reverse_lazy
from django import forms
from .forms import VisitForm
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponseRedirect


class FormAndListView(View):
    model = Visit
    form_class = VisitForm
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        visits = Visit.objects.all()[:5]
        return render(self.request, self.template_name, {"form": form, "visits": visits,})

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        visits = Visit.objects.all()[:5]
        if form.is_valid():
            form.save()
            # return redirect('visit:home')
            return HttpResponseRedirect(reverse_lazy('visit:home'))

        return render(self.request, self.template_name, {"form": form, "visits": visits,})


class VisitListView(ListView):
    model = Visit
    template_name = "visit_list.html"


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

