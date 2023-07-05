from django.urls import path
from .views import (
    VisitListView,
    VisitDetailView,
    VisitCreateView,
    VisitUpdateView,
    VisitDeleteView,
    FormAndListView,
)
from django.views.i18n import JavaScriptCatalog

app_name = "visit"
urlpatterns = [
    path("", FormAndListView.as_view(), name="home"),
    path("<int:pk>/delete/", VisitDeleteView.as_view(), name="visit_delete"),
    path("<int:pk>/edit/", VisitUpdateView.as_view(), name="visit_edit"),
    path("new/", VisitCreateView.as_view(), name="visit_new"),
    path("<int:pk>/", VisitDetailView.as_view(), name="visit_detail"),
    path("list/", VisitListView.as_view(), name="visit_list"),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='js-catlog'),
]
