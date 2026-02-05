from django.urls import path
from . import views
from .views import DashboardView
urlpatterns = [
    path("", DashboardView.as_view(), name="watch-dashboard"),
    path("add/", views.add_item, name="watch-add"),
    path("watched/<int:item_id>/", views.mark_watched, name="watch-watched"),
    path("rate/<int:item_id>/", views.rate_item, name="watch-rate"),
]
