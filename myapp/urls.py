from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('opening-hours/', views.OpeningHoursView.get, name='opening-hours')
]