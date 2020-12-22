from django.urls import path
from . import views

urlpatterns = [
    path('', views.professors, name='professors'),
    path('<int:professor_id>', views.professor, name='professor'),
]
