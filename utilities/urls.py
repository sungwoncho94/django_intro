from django.urls import path
from . import views


urlpatterns = [
    path('utilities/index/', views.index),
]
