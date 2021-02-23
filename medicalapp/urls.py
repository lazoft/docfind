from django.urls import path
from . import views
from .views import DoctorListView, HospitalListView, DieseaseListView

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('hospitals/', HospitalListView.as_view(), name='hospital-list'),
    path('diseases/', DieseaseListView.as_view(), name='disease-list')
]
