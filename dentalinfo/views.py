# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect

from dentalinfo.utils import ObjectCreateMixin, PageLinksMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from dentalinfo.forms import ServiceForm, PatientForm, DentistForm, TimeForm, AppointmentForm
from dentalinfo.models import Service, Patient, Dentist, Time, Appointment


# class ServiceList(View):
#     def get(self, request):
#         return render(request, 'dentalinfo/service_list.html', {'service_list': Service.objects.all()})
class ServiceList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Service
    permission_required = 'dentalinfo.view_service'


# class ServiceDetail(View):
#     def get(self, request, pk):
#         service = get_object_or_404(Service, pk = pk )
#         appointment_list = service.appointments.all()
#         return render(request,
#                       'dentalinfo/service_detail.html',
#                       {'service': service, 'appointment_list': appointment_list})
class ServiceDetail(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Service
    permission_required = 'dentalinfo.view_service'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        service = self.get_object()
        apppointment_list = service.appointments.all()
        context['appointment_list'] = apppointment_list
        return context


# class ServiceCreate(ObjectCreateMixin, View):
#     form_class = ServiceForm
#     template_name = 'dentalinfo/service_form.html'
class ServiceCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = ServiceForm
    model = Service
    permission_required = 'dentalinfo.add_service'


# class ServiceUpdate(View):
#     form_class = ServiceForm
#     model = Service
#     template_name = 'dentalinfo/service_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk)
#
#     def get(self, request, pk):
#         service = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance= service),
#             'service': service,
#         }
#         return render(
#             request, self.template_name, context)
#
#     def post(self, request, pk):
#         service = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance= service)
#         if bound_form.is_valid():
#             new_service = bound_form.save()
#             return redirect(new_service)
#         else:
#             context = {
#                 'form': bound_form,
#                 'service': service,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context)
class ServiceUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = ServiceForm
    model = Service
    template_name = 'dentalinfo/service_form_update.html'
    permission_required = 'dentalinfo.change_service'


# class ServiceDelete(View):
#     def get(self, request, pk):
#         service = self.get_object(pk)
#         appointments = service.appointments.all()
#         if appointments.count() > 0:
#             return render(request, 'dentalinfo/service_refuse_delete.html',
#                           {'service': service, 'appointments': appointments,})
#         else:
#             return render(request, 'dentalinfo/service_confirm_delete.html',
#                           {'service': service})
#
#     def get_object(self, pk):
#         return get_object_or_404(Service, pk=pk)
#
#     def post(self, request, pk):
#         service = self.get_object(pk)
#         service.delete()
#         return redirect('dentalinfo_service_list_urlpattern')
class ServiceDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Service
    success_url = reverse_lazy('dentalinfo_service_list_urlpattern')
    permission_required = 'dentalinfo.delete_instructor'

    def get(self, request, pk):
        service = get_object_or_404(Service, pk = pk)
        appointments = service.appointments.all()
        if appointments.count() > 0:
            return render(request, 'dentalinfo/service_refuse_delete.html',
                          {'service': service, 'appointments': appointments,})
        else:
            return render(request, 'dentalinfo/service_confirm_delete.html',
                          {'service': service})

# class PatientList(View):
#     page_kwarg = 'page'
#     paginate_by = 25
#     template_name = 'dentalinfo/patient_list.html'
#
#     def get(self, request):
#         patients = Patient.objects.all()
#         paginator = Paginator(patients,self.paginate_by)
#         page_number = request.GET.get(self.page_kwarg)
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(pkw=self.page_kwarg, n=page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'patient_list': page,
#         }
#         return render(request, self.template_name, context)
class PatientList(LoginRequiredMixin, PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 25
    model = Patient
    permission_required = 'dentalinfo.view_patient'


# class PatientDetail(View):
#     def get(self, request, pk):
#         patient = get_object_or_404(Patient, pk=pk)
#         appointment_list = patient.appointments.all()
#         return render(request,
#                       'dentalinfo/patient_detail.html',
#                       {'patient': patient, 'appointment_list': appointment_list})
class PatientDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Patient
    permission_required = 'dentalinfo.view_patient'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        patient = self.get_object()
        apppointment_list = patient.appointments.all()
        context['appointment_list'] = apppointment_list
        return context


# class PatientCreate(ObjectCreateMixin, View):
#     form_class = PatientForm
#     template_name = 'dentalinfo/patient_form.html'
class PatientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PatientForm
    model = Patient
    permission_required = 'dentalinfo.add_patient'


# class PatientUpdate(View):
#     form_class = PatientForm
#     model = Patient
#     template_name = 'dentalinfo/patient_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk)
#
#     def get(self, request, pk):
#         patient = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance= patient),
#             'patient': patient,
#         }
#         return render(
#             request, self.template_name, context)
#
#     def post(self, request, pk):
#         patient = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance= patient)
#         if bound_form.is_valid():
#             new_patient = bound_form.save()
#             return redirect(new_patient)
#         else:
#             context = {
#                 'form': bound_form,
#                 'patient': patient,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context)
class PatientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PatientForm
    model = Patient
    template_name = 'dentalinfo/patient_form_update.html'
    permission_required = 'dentalinfo.change_patient'


# class PatientDelete(View):
#     def get(self, request, pk):
#         patient = self.get_object(pk)
#         appointments = patient.appointments.all()
#         if appointments.count() > 0:
#             return render(request, 'dentalinfo/patient_refuse_delete.html',
#                           {'patient': patient, 'appointments': appointments,})
#         else:
#             return render(request, 'dentalinfo/patient_confirm_delete.html',
#                           {'patient': patient})
#
#     def get_object(self, pk):
#         return get_object_or_404(Patient, pk=pk)
#
#     def post(self, request, pk):
#         patient = self.get_object(pk)
#         patient.delete()
#         return redirect('dentalinfo_patient_list_urlpattern')
class PatientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('dentalinfo_patient_list_urlpattern')
    permission_required = 'dentalinfo.delete_patient'
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        appointments = patient.appointments.all()
        if appointments.count() > 0:
            return render(request, 'dentalinfo/patient_refuse_delete.html',
                            {'patient': patient, 'appointments': appointments,})
        else:
            return render(request, 'dentalinfo/patient_confirm_delete.html',
                          {'patient': patient})


# class DentistList(View):
#     def get(self, request):
#         return render(request, 'dentalinfo/dentist_list.html', {'dentist_list': Dentist.objects.all()})
class DentistList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Dentist
    permission_required = 'dentalinfo.view_dentist'


# class DentistDetail(View):
#     def get(self, request, pk):
#         dentist = get_object_or_404(Dentist, pk=pk)
#         appointment_list = dentist.appointments.all()
#         return render(request,
#                       'dentalinfo/dentist_detail.html',
#                       {'dentist': dentist, 'appointment_list': appointment_list})
class DentistDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Dentist
    permission_required = 'dentalinfo.view_dentist'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dentist = self.get_object()
        apppointment_list = dentist.appointments.all()
        context['appointment_list'] = apppointment_list
        return context


# class DentistCreate(ObjectCreateMixin, View):
#     form_class = DentistForm
#     template_name = 'dentalinfo/dentist_form.html'
class DentistCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DentistForm
    model = Dentist
    permission_required = 'dentalinfo.add_dentist'


# class DentistUpdate(View):
#     form_class = DentistForm
#     model = Dentist
#     template_name = 'dentalinfo/dentist_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk)
#
#     def get(self, request, pk):
#         dentist = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance= dentist),
#             'dentist': dentist,
#         }
#         return render(
#             request, self.template_name, context)
#
#     def post(self, request, pk):
#         dentist = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance= dentist)
#         if bound_form.is_valid():
#             new_dentist = bound_form.save()
#             return redirect(new_dentist)
#         else:
#             context = {
#                 'form': bound_form,
#                 'dentist': dentist,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context)
class DentistUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DentistForm
    model = Dentist
    template_name = 'dentalinfo/dentist_form_update.html'
    permission_required = 'dentalinfo.change_dentist'


# class DentistDelete(View):
#     def get(self, request, pk):
#         dentist = self.get_object(pk)
#         appointments = dentist.appointments.all()
#         if appointments.count() > 0:
#             return render(request, 'dentalinfo/dentist_refuse_delete.html',
#                           {'dentist': dentist, 'appointments': appointments,})
#         else:
#             return render(request, 'dentalinfo/dentist_confirm_delete.html',
#                           {'dentist': dentist})
#
#     def get_object(self, pk):
#         return get_object_or_404(Dentist, pk=pk)
#
#     def post(self, request, pk):
#         dentist = self.get_object(pk)
#         dentist.delete()
#         return redirect('dentalinfo_dentist_list_urlpattern')
class DentistDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dentist
    success_url = reverse_lazy('dentalinfo_dentist_list_urlpattern')
    permission_required = 'dentalinfo.delete_dentist'
    def get(self, request, pk):
        dentist = get_object_or_404(Dentist, pk=pk)
        appointments = dentist.appointments.all()
        if appointments.count() > 0:
            return render(request, 'dentalinfo/dentist_refuse_delete.html',
                          {'dentist': dentist, 'appointments': appointments,})
        else:
            return render(request, 'dentalinfo/dentist_confirm_delete.html',
                          {'dentist': dentist})



# class TimeList(View):
#     def get(self, request):
#         return render(request, 'dentalinfo/time_list.html', {'time_list': Time.objects.all()})
class TimeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Time
    permission_required = 'dentalinfo.view_time'


# class TimeDetail(View):
#     def get(self, request, pk):
#         time = get_object_or_404(Time, pk=pk)
#         appointment_list = time.appointments.all()
#         return render(request,
#                       'dentalinfo/time_detail.html',
#                       {'time': time, 'appointment_list': appointment_list})
class TimeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Time
    permission_required = 'dentalinfo.view_time'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        time = self.get_object()
        year = time.year
        month = time.month
        day = time.day
        hour = time.hour
        appointment_list = time.appointments.all()
        context['year'] = year
        context['month'] = month
        context['day'] = day
        context['hour'] = hour
        context['appointment_list'] = appointment_list
        return context


# class TimeCreate(ObjectCreateMixin, View):
#     form_class = TimeForm
#     template_name = 'dentalinfo/time_form.html'
class TimeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TimeForm
    model = Time
    permission_required = 'dentalinfo.add_time'


# class TimeUpdate(View):
#     form_class = TimeForm
#     model = Time
#     template_name = 'dentalinfo/time_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk)
#
#     def get(self, request, pk):
#         time = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance=time),
#             'time': time,
#         }
#         return render(
#             request, self.template_name, context)
#
#     def post(self, request, pk):
#         time = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=time)
#         if bound_form.is_valid():
#             new_time = bound_form.save()
#             return redirect(new_time)
#         else:
#             context = {
#                 'form': bound_form,
#                 'time': time,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context)
class TimeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TimeForm
    model = Time
    template_name = 'dentalinfo/time_form_update.html'
    permission_required = 'dentalinfo.change_time'


# class TimeDelete(DeleteView):
#     def get(self, request, pk):
#         time = self.get_object(pk)
#         return render(request, 'dentalinfo/time_confirm_delete.html', {'time': time})
#
#     def get_object(self, pk):
#         hour = get_object_or_404(Time, pk = pk)
#         return hour
#
#     def post(self, request, pk):
#         time = self.get_object(pk)
#         time.delete()
#         return redirect('dentalinfo_time_list_urlpattern')
class TimeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Time
    success_url = reverse_lazy('dentalinfo_time_list_urlpattern')
    permission_required = 'dentalinfo.delete_time'
    def get(self, request, pk):
        time = get_object_or_404(Time, pk=pk)
        appointments = time.appointments.all()
        if appointments.count() > 0:
            return render(request, 'dentalinfo/time_refuse_delete.html',
                          {'time': time, 'appointments': appointments,})
        else:
            return render(request, 'dentalinfo/time_confirm_delete.html',
                          {'time': time})


# class AppointmentList(View):
#     page_kwarg = 'page'
#     paginate_by = 10
#     template_name = 'dentalinfo/appointment_list.html'
#
#     def get(self, request):
#         appointments = Appointment.objects.all()
#         paginator = Paginator(
#             appointments,
#             self.paginate_by
#         )
#         page_number = request.GET.get(
#             self.page_kwarg
#         )
#         try:
#             page = paginator.page(page_number)
#         except PageNotAnInteger:
#             page = paginator.page(1)
#         except EmptyPage:
#             page = paginator.page(
#                 paginator.num_pages)
#         if page.has_previous():
#             prev_url = "?{pkw}={n}".format(
#                 pkw=self.page_kwarg,
#                 n=page.previous_page_number())
#         else:
#             prev_url = None
#         if page.has_next():
#             next_url = "?{pkw}={n}".format(
#                 pkw=self.page_kwarg,
#                 n=page.next_page_number())
#         else:
#             next_url = None
#         context = {
#             'is_paginated':
#                 page.has_other_pages(),
#             'next_page_url': next_url,
#             'paginator': paginator,
#             'previous_page_url': prev_url,
#             'appointment_list': page,
#         }
#         return render(
#             request, self.template_name, context)
class AppointmentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Appointment
    permission_required = 'dentalinfo.view_appointment'


# class AppointmentDetail(View):
#     def get(self, request, pk):
#         appointment = get_object_or_404(Appointment, pk = pk)
#         # patient = appointment.patient
#         # service = appointment.service
#         # dentist = appointment.dentist
#         return render(request,
#                       'dentalinfo/appointment_detail.html',
#                       {'appointment': appointment})
class AppointmentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Appointment
    permission_required = 'dentalinfo.view_appointment'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        appointment = self.get_object()
        patient = appointment.patient
        service = appointment.service
        dentist = appointment.dentist
        time = appointment.time
        context['patient'] = patient
        context['service'] = service
        context['dentist'] = dentist
        context['time'] = time
        return context


# class AppointmentCreate(ObjectCreateMixin, View):
#     form_class = AppointmentForm
#     template_name = 'dentalinfo/appointment_form.html'
class AppointmentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AppointmentForm
    model = Appointment
    permission_required = 'dentalinfo.add_appointment'


# class AppointmentUpdate(View):
#     form_class = AppointmentForm
#     model = Appointment
#     template_name = 'dentalinfo/appointment_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk)
#
#     def get(self, request, pk):
#         appointment = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance=appointment),
#             'appointment': appointment,
#         }
#         return render(
#             request, self.template_name, context)
#
#     def post(self, request, pk):
#         appointment = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=appointment)
#         if bound_form.is_valid():
#             new_appointment = bound_form.save()
#             return redirect(new_appointment)
#         else:
#             context = {
#                 'form': bound_form,
#                 'appointment': appointment,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context)
class AppointmentUpdate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AppointmentForm
    model = Appointment
    template_name = 'dentalinfo/appointment_form_update.html'
    permission_required = 'dentalinfo.add_appointment'


# class AppointmentDelete(View):
#     def get(self, request, pk):
#         appointment = self.get_object(pk)
#         return render(request, 'dentalinfo/appointment_confirm_delete.html', {'appointment': appointment})
#
#     def get_object(self, pk):
#         patient = get_object_or_404(Appointment, pk = pk)
#         return patient
#
#     def post(self, request, pk):
#         appointment = self.get_object(pk)
#         appointment.delete()
#         return redirect('dentalinfo_appointment_list_urlpattern')
class AppointmentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Appointment
    success_url = reverse_lazy('dentalinfo_appointment_list_urlpattern')
    permission_required = 'dentalinfo.delete_appointment'