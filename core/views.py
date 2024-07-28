from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.urls import reverse
from .forms import PatientForm
from django.db.models import Q

def home(request):
    return render(request, 'core/home.html')

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'core/register_patient.html', {'form': form})

def check_registration(request):
    query = request.POST.get('query', '')
    patient = None
    
    if query:
        patient = Patient.objects.filter(
            Q(email__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).first()
    
    patients = Patient.objects.all()  # Fetch all patients

    return render(request, 'core/check_registration.html', {
        'patient': patient,
        'patients': patients
    })

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()
    return redirect(reverse('check_registration'))

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.first_name = request.POST.get('first_name', patient.first_name)
        patient.last_name = request.POST.get('last_name', patient.last_name)
        patient.email = request.POST.get('email', patient.email)
        patient.phone_number = request.POST.get('phone_number', patient.phone_number)
        patient.save()
        return redirect(reverse('check_registration'))
    return render(request, 'core/edit_patient.html', {'patient': patient})
