from django.urls import path
from main import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("add/", views.add_view, name="add"),
    path('add/upload/', views.upload, name = "upload"),
    path('search_view/', views.search_view, name = "search_view"),
]
