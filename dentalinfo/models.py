from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Service(models.Model):
    service_id = models.AutoField(primary_key = True)
    service_type = models.CharField(max_length=45, blank=True, default='', unique=True)

    def __str__(self):
        return '%s' % self.service_type

    def get_absolute_url(self):
        return reverse('dentalinfo_service_detail_urlpattern', kwargs = {'pk': self.pk})

    def get_update_url(self):
        return reverse('dentalinfo_service_update_urlpattern', kwargs= {'pk': self.pk})

    def get_delete_url(self):
        return reverse('dentalinfo_service_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['service_type']


class Patient(models.Model):
    patient_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('dentalinfo_patient_detail_urlpattern', kwargs = {'pk': self.pk})

    def get_update_url(self):
        return reverse('dentalinfo_patient_update_urlpattern', kwargs= {'pk': self.pk})

    def get_delete_url(self):
        return reverse('dentalinfo_patient_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name = 'unique_patient')
        ]


class Dentist(models.Model):
    dentist_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.ForeignKey(Service, on_delete= models.PROTECT)

    def __str__(self):
        return '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)

    def get_absolute_url(self):
        return reverse('dentalinfo_dentist_detail_urlpattern', kwargs = {'pk': self.pk})

    def get_update_url(self):
        return reverse('dentalinfo_dentist_update_urlpattern', kwargs= {'pk': self.pk})

    def get_delete_url(self):
        return reverse('dentalinfo_dentist_delete_urlpattern', kwargs= {'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_dentist')
        ]


class Year(models.Model):
    year_id = models.AutoField(primary_key = True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.year

    class Meta:
        ordering = ['year']


class Month(models.Model):
    month_id = models.AutoField(primary_key = True)
    month = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.month

    class Meta:
        ordering = ['month']


class Day(models.Model):
    day_id = models.AutoField(primary_key = True)
    day = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.day

    class Meta:
        ordering = ['day']


class Hour(models.Model):
    hour_id = models.AutoField(primary_key = True)
    hour = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.hour

    class Meta:
        ordering = ['hour']


class Time(models.Model):
    time_id = models.AutoField(primary_key = True)
    year = models.ForeignKey(Year, related_name='times', on_delete= models.PROTECT)
    month = models.ForeignKey(Month, related_name='times', on_delete= models.PROTECT)
    day = models.ForeignKey(Day, related_name='times', on_delete= models.PROTECT)
    hour = models.ForeignKey(Hour, related_name='times', on_delete= models.PROTECT)

    def __str__(self):
        return '%s / %s / %s, %s' % (self.month, self.day, self.year, self.hour)

    def get_absolute_url(self):
        return reverse('dentalinfo_time_detail_urlpattern', kwargs = {'pk': self.pk})

    def get_update_url(self):
        return reverse('dentalinfo_time_update_urlpattern', kwargs= {'pk': self.pk})

    def get_delete_url(self):
        return reverse('dentalinfo_time_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['month', 'day', 'year', 'hour']
        constraints = [
            UniqueConstraint(fields=['month', 'day', 'year', 'hour'], name = 'unique_time')
        ]


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key = True)
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete= models.PROTECT)
    service = models.ForeignKey(Service, related_name='appointments', on_delete= models.PROTECT)
    dentist = models.ForeignKey(Dentist, related_name='appointments', on_delete= models.PROTECT)
    time = models.ForeignKey(Time, related_name='appointments', on_delete= models.PROTECT)

    def __str__(self):
        return '%s - %s - %s (%s)' % (self.patient, self.service, self.dentist, self.time)

    def get_absolute_url(self):
        return reverse('dentalinfo_appointment_detail_urlpattern', kwargs = {'pk': self.pk})

    def get_update_url(self):
        return reverse('dentalinfo_appointment_update_urlpattern', kwargs= {'pk': self.pk})

    def get_delete_url(self):
        return reverse('dentalinfo_appointment_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['patient', 'service', 'dentist', 'time']
        constraints = [
            UniqueConstraint(fields=['patient', 'service', 'dentist', 'time'], name = 'unique_appointment')
        ]
