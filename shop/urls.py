from django.urls import path
from . import views


urlpatterns = [
    path("health/", views.health),
    path("info/", views.info),
    path("products/", views.product_list),
    path("products/<int:product_id>/", views.product_detail),
    path("statystyki/", views.statistics),
]
