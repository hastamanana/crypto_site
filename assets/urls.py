from . import views

from django.urls import path


urlpatterns = [
    path('assets/', views.assets, name='manage_assets')
]
