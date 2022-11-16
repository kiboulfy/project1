from django.urls import path

from . import views

urlpatterns = [
    path('', views.authen),
    path('adding/', views.adding),
]