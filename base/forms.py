from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ClearanceForm, StudentProfile, StaffProfile

class StudentRegistrationForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model=StudentProfile
        fields=['surname','othernames','directorate', 'department','program_of_study','study_mode','state_of_origin','profile_pic','id_card','student_file']
        widgets={
            'surname':forms.TextInput(attrs={'class':'form-control'}),
            'othernames':forms.TextInput(attrs={'class':'form-control'}),
            'directorate':forms.Select(attrs={'class':'form-control'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'program_of_study':forms.Select(attrs={'class':'form-control'}),
            'study_mode':forms.Select(attrs={'class':'form-control'}),
            'state_of_origin':forms.Select(attrs={'class':'form-control'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'id_card':forms.FileInput(attrs={'class':'form-control'}),
            'student_file':forms.FileInput(attrs={'class':'form-control'}),
        }

class StaffProfileForm(forms.ModelForm):

    class Meta:
        model=StaffProfile
        fields=['user_id','firstname','lastname','sex','age','job_status','office_number','educational_position','email','profile_picture']
        widgets={
            'user_id':forms.TextInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'sex':forms.Select(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'job_status':forms.TextInput(attrs={'class':'form-control'}),
            'office_number':forms.TextInput(attrs={'class':'form-control'}),
            'educational_position':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'profile_picture':forms.FileInput(attrs={'class':'form-control'}),
        }

class StudentClearanceForm(forms.ModelForm):

    class Meta:
        model=ClearanceForm
        fields=["surname",'othernames','sex','department','program_of_study','date_of_birth','date_of_completion','libary_registration_num','last_room_num',
            'phone_number','mat_receipt_num','convocation_gown_receipt_num','mat_receipt_num_date','alumini_receipt_num','alumini_receipt_num_date',
            'school_fees_receipt_year_1','school_fees_receipt_year_1_date','convocation_gown_receipt_num_date','school_fees_receipt_year_2',
            'school_fees_receipt_year_2_date','enterpreneur_receipt_num','enterpreneur_receipt_num_date','certificate_processing_fee_receipt',
            'certificate_processing_fee_receipt_date']
        widgets={
            'surname':forms.TextInput(attrs={'class':'form-control'}),
            'othernames':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'sex':forms.Select(attrs={'class':'form-control'}),
            'program_of_study':forms.Select(attrs={'class':'form-control'}),
            'libary_registration_num':forms.NumberInput(attrs={'class':'form-control'}),
            'convocation_gown_receipt_num':forms.NumberInput(attrs={'class':'form-control'}),
            'convocation_gown_receipt_num_date':forms.DateInput(attrs=dict(type='date')),
            'mat_receipt_num':forms.NumberInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'last_room_num':forms.TextInput(attrs={'class':'form-control'}),
            'school_fees_receipt_year_1':forms.NumberInput(attrs={'class':'form-control'}),
            'school_fees_receipt_year_2':forms.NumberInput(attrs={'class':'form-control'}),
            'alumini_receipt_num':forms.NumberInput(attrs={'class':'form-control'}),
            'enterpreneur_receipt_num':forms.NumberInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs=dict(type='date')),
            'date_of_completion':forms.DateInput(attrs=dict(type='date')),
            'mat_receipt_num_date':forms.DateInput(attrs=dict(type='date')),
            'alumini_receipt_num_date':forms.DateInput(attrs=dict(type='date')),
            'school_fees_receipt_year_2_date':forms.DateInput(attrs=dict(type='date')),
            'school_fees_receipt_year_1_date':forms.DateInput(attrs=dict(type='date')),
            'enterpreneur_receipt_num_date':forms.DateInput(attrs=dict(type='date')),
            'alumini_receipt_num_date':forms.DateInput(attrs=dict(type='date')),
            'certificate_processing_fee_receipt':forms.NumberInput(attrs={'class':'form-control'}),
            'certificate_processing_fee_receipt_date':forms.DateInput(attrs=dict(type='date')),
        }