from django.urls import path
from firstbook import views, comment_views, study_views


urlpatterns = [
    path('study/new/', study_views.new_study, name='new_study'),
    path('study/edit/<str:study>', study_views.study_update, name='study_edit'),
    path('study/delete/<str:study>', study_views.study_delete, name='study_delete'),
    path('study/list/', study_views.study_list, name='study_list'),
    path('study/graph/', views.graph, name='study_rate'),
    path('comment/new', comment_views.new_comment, name='new_comment'),
    path('comment/list/<str:study>/', comment_views.comment_list, name='comment_list'),
]
