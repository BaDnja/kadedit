from django.urls import path, include
from . import views

work_statuses_patterns = [
    path('', views.work_statuses, name='work_statuses'),
    path('status/<int:status_id>/', views.single_work_status, name='single_work_status'),
    path('status/add', views.work_status_add, name="work_status_add"),
    path('status/update/<int:status_id>/', views.work_status_update, name="work_status_update"),
    path('status/delete/<int:status_id>/', views.work_status_delete, name="work_status_delete"),
]

academic_title_patterns = [
    path('', views.academic_titles, name='academic_titles'),
]

urlpatterns = [
    path('', views.professors, name='professors'),
    path('<int:professor_id>', views.professor, name='professor'),
    path('work_statuses/', include(work_statuses_patterns)),
    path('academic_titles/', include(academic_title_patterns)),
]
