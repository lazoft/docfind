from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Doctor, Hospital, Field, Disease


def home(request):
    return render(request, 'medicalapp/home.html')


class DoctorListView(ListView):
    model = Doctor
    template_name = 'medicalapp/doctors_list.html'
    context_object_name = 'doctors'
    ordering = ['name']
    paginate_by = 10


class HospitalListView(ListView):
    model = Hospital
    template_name = 'medicalapp/hospital_list.html'
    context_object_name = 'hospitals'
    ordering = ['name']
    paginate_by = 10


class DieseaseListView(ListView):
    model = Disease
    template_name = 'medicalapp/disease_list.html'
    context_object_name = 'diseases'
    ordering = ['name']
    paginate_by = 10
