from django.urls import path
from . import views
from .views import (DoctorListView, HospitalListView,
                    DieseaseListView, SearchListView, DoctorDetailView)

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('hospitals/', HospitalListView.as_view(), name='hospital-list'),
    path('diseases/', DieseaseListView.as_view(), name='disease-list'),
    path('search/', SearchListView.as_view(), name='search-list'),
]
