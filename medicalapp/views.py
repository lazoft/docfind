from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Doctor


def home(request):
    return render(request, 'medicalapp/home.html')


class DoctorListView(ListView):
    model = Doctor
    template_name = 'medicalapp/doctors_list.html'
    context_object_name = 'doctors'
    ordering = ['name']
    paginate_by = 10
