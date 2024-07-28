from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_patient, name='register_patient'),
    path('check/', views.check_registration, name='check_registration'),
    path('check_registration/', views.check_registration, name='check_registration'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
]
