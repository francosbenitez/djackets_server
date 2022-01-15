## This file is created to be more clean.
## Specifically, to have each of the Django apps separated.

from django.urls import path, include

from product import views

urlpatterns = [
  path('latest-products/', views.LatestProductsList.as_view())
]