from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    ManufacturerListView,
    DriverListView, DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path("driver/<int:pk>", DriverDetailView.as_view(), name="driver-detail"),
]

app_name = "taxi"
