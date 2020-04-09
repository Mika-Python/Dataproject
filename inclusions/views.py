from django.shortcuts import render, redirect
from .models import Patient
from .forms import NewPatient, NewPathology


def new_patient(request):
    if request.method == 'POST':
        form = NewPatient(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')


    else:
        form = NewPatient()
    return render(request, "inclusion/new_patient.html", {'form': form})


def patient_delete(request, patient):

    instance = Patient.objects.get(identification=patient)
    patient_name = instance.name
    instance.delete()

    return render(request, 'firstbook/study_delete.html', {'patient': patient_name})

def new_pathology(request):
    if request.method == 'POST':
        form = NewPathology(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')


    else:
        form = NewPathology()
    return render(request, "inclusion/new_pathology.html", {'form': form})


def patient_list(request, study):
    patient = []
    for i in Patient.objects.filter(studies__name=study):
        patient.append(i)

    return render(request, "inclusion/patient_list.html", {'list': patient, 'study': study})