from django.urls import path, include
from generate.views import home

app_name = "generate"
urlpatterns = [
    path("", home, name="home"),
]
