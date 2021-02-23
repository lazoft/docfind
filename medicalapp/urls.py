from django.urls import path
from . import views
from .views import DoctorListView

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list')
]
