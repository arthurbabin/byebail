from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
    path("reviews",views.reviews, name="reviews")
]