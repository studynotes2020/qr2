from django.urls import path, include
# from generate.views import home
from .views import HomeView

app_name = "generate"
urlpatterns = [
    # path("", home, name="home"),
    path('', HomeView.as_view(), name='home'),
]
