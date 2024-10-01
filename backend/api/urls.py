from django.urls import path
from . import views

urlpatterns = [
    path("listings/", views.ListingsView.as_view(), name="view-listings"),
    path("listings/create/", views.ListingCreate.as_view(), name="create-listing"),
    path("listings/delete/<int:pk>/", views.ListingDelete.as_view(), name="delete-listing"),
]
