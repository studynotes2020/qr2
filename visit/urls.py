from django.urls import path
from .views import (
    VisitListView,
    VisitDetailView,
    VisitCreateView,
    VisitUpdateView,
    VisitDeleteView,
)

app_name = "visit"
urlpatterns = [
    path("<int:pk>/delete/", VisitDeleteView.as_view(), name="visit_delete"),
    path("<int:pk>/edit/", VisitUpdateView.as_view(), name="visit_edit"),
    path("new/", VisitCreateView.as_view(), name="visit_new"),
    path("<int:pk>/", VisitDetailView.as_view(), name="visit_detail"),
    path("", VisitListView.as_view(), name="home"),
]
