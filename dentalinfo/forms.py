from django import forms
from dentalinfo.models import Service, Patient, Dentist, Time, Appointment


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def clean_service_type(self):
        return self.cleaned_data['service_type'].strip()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()
        return result


class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    # def clean_disambiguator(self):
    #     if len(self.cleaned_data['disambiguator']) == 0:
    #         result = self.cleaned_data['disambiguator']
    #     else:
    #         result = self.cleaned_data['disambiguator'].strip()
    #     return result


class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'