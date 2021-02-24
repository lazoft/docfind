from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Doctor, Hospital, Field, Disease
from django.db.models import Q


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


class SearchListView(ListView):
    model = Doctor
    template_name = 'medicalapp/search_list.html'
    ordering = ['name']
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        doctor_list = Doctor.objects.filter(Q(name__icontains=query) | Q(bio__icontains=query) | Q(
            fields__name__icontains=query) | Q(hospital__name__icontains=query) | Q(treats__name__icontains=query))

        return doctor_list
