from django.shortcuts import render
import logging
from django.contrib.auth import login, authenticate
from django.contrib import messages
from . import forms
from django.views.generic.edit import FormView

logger = logging.getLogger(__name__)


class SignupView(FormView):
    template_name = "signup.html"
    form_class = forms.CustomUserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        logger.info(
            "New signup for email=%s through SignupView", email
        )
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        messages.info(
            self.request, "You signed up successfully."
        )
        return response
