from django.shortcuts import render, redirect
from firstbook.forms import NewStudy
from firstbook.models import Study


def new_study(request):
    if request.method == 'POST':
        form = NewStudy(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')


    else:
        form = NewStudy()
    return render(request, "firstbook/new_study.html", {'form': form})


def study_list(request):
    study_list = []
    for i in Study.objects.all():
        study_list.append(i)

    return render(request, "firstbook/study_list.html", {'list': study_list})


def study_update(request, study):
    instance = Study.objects.get(name=study)

    if request.method == 'POST':
        form = NewStudy(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('study_list')

    else:
        form = NewStudy(instance=instance)

    return render(request, 'firstbook/edit_study.html', {'form': form})


def study_delete(request, study):

    instance = Study.objects.get(name=study)
    study_name = instance.name
    instance.delete()

    return render(request, 'firstbook/study_delete.html', {'study': study_name})