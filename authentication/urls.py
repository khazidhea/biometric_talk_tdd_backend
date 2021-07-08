from django.urls import path

from . import views

urlpatterns = [
    path('csrf/', views.csrf),
    path('register/', views.RegisterApi.as_view()),
]
