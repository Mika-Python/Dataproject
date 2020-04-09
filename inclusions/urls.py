from django.urls import path
from inclusions import views

urlpatterns = [
    path('patient/new/', views.new_patient, name='new_patient'),
    path('patient/list/<str:study>', views.patient_list, name='patient_list'),
    path('patient/pathology/new', views.new_pathology, name='new_pathology'),
    path('patient/delete//<str:patient>', views.patient_delete, name='patient_delete'),
]
