from . import views

from django.urls import path

urlpatterns = [
    path('', views.forecast_view, name='forecast_view'),
    path('data/', views.forecast_data, name='forecast_data'),
]
