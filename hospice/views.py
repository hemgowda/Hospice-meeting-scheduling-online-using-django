from django.shortcuts import render

# Create your views here.
from django.views import generic
from hospice.models import Hospice,Admit,Patient

class HospiceListView(generic.ListView):
    model = Hospice
    template_name = 'Hospice_list.html'

class PatientListView(generic.ListView):
    model = Patient
    template_name = 'Patient_list.html'
class AdmitListView(generic.ListView):
    model = Admit
    template_name = 'Admit_list.html'