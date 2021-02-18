from django.urls import path, include
from . import views

engagements_patterns = [
    path('', views.engagements, name='engagements'),
    path('engagement/<int:engagement_id>/', views.single_engagement, name='single_engagement'),
    path('engagement/add', views.engagement_add, name='engagement_add'),
    path('engagement/update/<int:engagement_id>/', views.engagement_update, name='engagement_update'),
    path('engagement/delete/<int:engagement_id>/', views.engagement_delete, name='engagement_delete'),
    path('search/', views.engagement_search, name='engagement_search')
]

work_statuses_patterns = [
    path('', views.work_statuses, name='work_statuses'),
    path('status/<int:status_id>/', views.single_work_status, name='single_work_status'),
    path('status/add', views.work_status_add, name="work_status_add"),
    path('status/update/<int:status_id>/', views.work_status_update, name="work_status_update"),
    path('status/delete/<int:status_id>/', views.work_status_delete, name="work_status_delete"),
    path('search/', views.work_status_search, name="work_status_search")
]

academic_title_patterns = [
    path('', views.academic_titles, name='academic_titles'),
    path('title/<int:title_id>/', views.single_academic_title, name='single_academic_title'),
    path('title/add', views.academic_title_add, name="academic_title_add"),
    path('title/update/<int:title_id>/', views.academic_title_update, name='academic_title_update'),
    path('title/delete/<int:title_id>/', views.academic_title_delete, name='academic_title_delete'),
    path('search/', views.academic_title_search, name='academic_title_search'),
]

professors_patterns = [
    path('', views.professors, name='professors'),
    path('professor/<int:professor_id>/', views.professor, name='professor'),
    path('professor/add/', views.professor_add, name='professor_add'),
    path('professor/update/<int:professor_id>/', views.professor_update, name='professor_update'),
    path('professor/delete/<int:professor_id>/', views.professor_delete, name='professor_delete'),
    path('professor/deactivate/<int:professor_id>/', views.professor_deactivate, name='professor_deactivate'),
    path('search/', views.professor_search, name='professor_search'),
]

urlpatterns = [
    path('', include(professors_patterns)),
    path('work_statuses/', include(work_statuses_patterns)),
    path('academic_titles/', include(academic_title_patterns)),
    path('engagements/', include(engagements_patterns)),
]
