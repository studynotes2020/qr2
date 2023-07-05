"""qr2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from . import admin
from django.urls import path, include
from django.views.generic import RedirectView
import accounts.views
import accounts.forms
from django.contrib.auth import views as auth_views

import sse_app.views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('guard-admin/', admin.guard_admin.urls),
    # path('resident-admin/', admin.resident_admin.urls),
    path('signup/', accounts.views.SignupView.as_view(), name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            form_class=accounts.forms.AuthenticationForm,
        ),
        name="login",
    ),

    # path("", RedirectView.as_view(url="qr-code-demo/", permanent=True)),
    # path("qr-code-demo/", include("qr_code_demo.urls", namespace="qr_code_demo")),
    # path("qr-code/", include("qr_code.urls", namespace="qr_code")),

    path("visit/", include("visit.urls", namespace="visit")),
    path("generate/", include("generate.urls", namespace="generate")),
    path('stream/', sse_app.views.stream, name='stream'),
    path("news/", include("news.urls", namespace="news")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
