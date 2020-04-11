from django.urls import path

urlpatterns = [
    path('study/new/', study_views.new_study, name='new_study'),
]