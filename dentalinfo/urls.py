from django.urls import path
from dentalinfo.views import (
    ServiceList,
    ServiceDetail,
    ServiceCreate,
    ServiceUpdate,
    ServiceDelete,

    PatientList,
    PatientDetail,
    PatientCreate,
    PatientUpdate,
    PatientDelete,

    DentistList,
    DentistDetail,
    DentistCreate,
    DentistUpdate,
    DentistDelete,

    TimeList,
    TimeDetail,
    TimeCreate,
    TimeUpdate,
    TimeDelete,

    AppointmentList,
    AppointmentDetail,
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentDelete,
)

urlpatterns = [
    path('service/', ServiceList.as_view(), name = 'dentalinfo_service_list_urlpattern'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name = 'dentalinfo_service_detail_urlpattern'),
    path('service/create/', ServiceCreate.as_view(), name = 'dentalinfo_service_create_urlpattern'),
    path('service/<int:pk>/update/', ServiceUpdate.as_view(), name = 'dentalinfo_service_update_urlpattern'),
    path('service/<int:pk>/delete/', ServiceDelete.as_view(), name = 'dentalinfo_service_delete_urlpattern'),

    path('patient/', PatientList.as_view(), name = 'dentalinfo_patient_list_urlpattern'),
    path('patient/<int:pk>/', PatientDetail.as_view(), name = 'dentalinfo_patient_detail_urlpattern'),
    path('patient/create/', PatientCreate.as_view(), name = 'dentalinfo_patient_create_urlpattern'),
    path('patient/<int:pk>/update/', PatientUpdate.as_view(), name = 'dentalinfo_patient_update_urlpattern'),
    path('patient/<int:pk>/delete/', PatientDelete.as_view(), name = 'dentalinfo_patient_delete_urlpattern'),

    path('dentist/', DentistList.as_view(), name = 'dentalinfo_dentist_list_urlpattern'),
    path('dentist/<int:pk>/', DentistDetail.as_view(), name = 'dentalinfo_dentist_detail_urlpattern'),
    path('dentist/create/', DentistCreate.as_view(), name = 'dentalinfo_dentist_create_urlpattern'),
    path('dentist/<int:pk>/update/', DentistUpdate.as_view(), name = 'dentalinfo_dentist_update_urlpattern'),
    path('dentist/<int:pk>/delete/', DentistDelete.as_view(), name = 'dentalinfo_dentist_delete_urlpattern'),

    path('time/', TimeList.as_view(), name = 'dentalinfo_time_list_urlpattern'),
    path('time/<int:pk>/', TimeDetail.as_view(), name = 'dentalinfo_time_detail_urlpattern'),
    path('time/create/', TimeCreate.as_view(), name = 'dentalinfo_time_create_urlpattern'),
    path('time/<int:pk>/update/', TimeUpdate.as_view(), name = 'dentalinfo_time_update_urlpattern'),
    path('time/<int:pk>/delete/', TimeDelete.as_view(), name = 'dentalinfo_time_delete_urlpattern'),

    path('appointment/', AppointmentList.as_view(), name = 'dentalinfo_appointment_list_urlpattern'),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name = 'dentalinfo_appointment_detail_urlpattern'),
    path('appointment/create/', AppointmentCreate.as_view(), name = 'dentalinfo_appointment_create_urlpattern'),
    path('appointment/<int:pk>/update/', AppointmentUpdate.as_view(), name = 'dentalinfo_appointment_update_urlpattern'),
    path('appointment/<int:pk>/delete/', AppointmentDelete.as_view(), name = 'dentalinfo_appointment_delete_urlpattern'),

]
