from . import views

from django.urls import path

urlpatterns = [
    path('forecast/', views.forecast, name='forecast'),
]
