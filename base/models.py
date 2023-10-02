from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DEPARTMENT_CHOICE=(
    ('Computer Science and Information Technology','Computer Science and Information Technology'),
    ('Mechanical Engineering Technology','Mechanical Engineering Technology'),
    ('Electrical Engineering','Electrical Engineering'),
    ('Industrial Safety','Industrial Safety'),
    ('Environmentl Technology','Environmentl Technology'),
    ('Mineral and Petroleum Resources','Mineral and Petroleum Resources'),
    ('Petroleum and Natural Gas Processing Technology','Petroleum and Natural Gas Processing Technology'),
    ('Petroleum Engineering and Geoscience','Petroleum Engineering and Geoscience'),
    ('Petroleum Marketing and Business Studies','Petroleum Marketing and Business Studies'),
    ('Science Laboratory Technology','Science Laboratory Technology'),
    ('Welding Engineering and Offshore Technology','Welding Engineering and Offshore Technology'),
    ('Computer Engineering Technoloy','Computer Engineering Technoloy'),
    ('Mechatronics','Mechatronics')
)
STUDY_MODE_CHOICES=(
    ('Part Time','Part Time'),
    ('Full Time','Full Time')
)
DIRECTORATE_CHOICES=(
    ('Science','Science'),
    ('Engineering','Engineering')
)
PROGRAM_OF_STUDY_CHOICES=(
    ('ND','ND'),
    ('HND','HND')
)
SEX_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)
STATE_OF_ORIGIN_CHOICES=(
    ('D','Delta'),
    ('E','Edo')
)


class StudentProfile(models.Model):
    surname=models.CharField(max_length=30)
    othernames= models.CharField(max_length=30)
    directorate=models.CharField(choices=DIRECTORATE_CHOICES, max_length=12)
    department= models.CharField(choices=DEPARTMENT_CHOICE, max_length=50)
    state_of_origin=models.CharField(max_length=50,choices=STATE_OF_ORIGIN_CHOICES)
    program_of_study= models.CharField(choices=PROGRAM_OF_STUDY_CHOICES, max_length=3)
    study_mode=models.CharField(choices=STUDY_MODE_CHOICES, max_length=10)
    posted_by= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile-pics/', verbose_name='Passport photo', null=True)
    id_card=models.ImageField(upload_to='id-img', verbose_name='ID card', null=True)
    student_file=models.FileField(upload_to='student-file/', verbose_name='Student documents', null=True)

    def __str__(self):
        return f"({self.pk}). {self.surname}\'s profile"
    

class StaffProfile(models.Model):
    user_id=models.CharField(max_length=15, unique=True)
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    sex=models.CharField(choices=SEX_CHOICES,max_length=6)
    age=models.IntegerField()
    job_status=models.CharField(max_length=15)
    office_number=models.CharField(max_length=30)
    educational_position=models.CharField(max_length=30)
    email=models.EmailField()
    posted_by= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile-pics/', null=True)

    def __str__(self):
        return f'({self.pk}). {self.user_id} Staff'
    

class ClearanceForm(models.Model):
    surname=models.CharField(max_length=30)
    othernames=models.CharField(max_length=30)
    sex=models.CharField(choices=SEX_CHOICES,max_length=8, null=True)
    department=models.CharField(choices=DEPARTMENT_CHOICE, max_length=50)
    program_of_study= models.CharField(choices=PROGRAM_OF_STUDY_CHOICES, max_length=3, null=True)
    date_of_birth=models.DateField('Date of birth',auto_now_add=False, auto_now=False,)
    date_of_completion=models.DateField('Date of completion ',auto_now_add=False, auto_now=False)
    libary_registration_num=models.IntegerField(verbose_name='library registration NO',null=True)
    last_room_num=models.CharField(max_length=10, null=True, blank=True, verbose_name='Last room NO')
    phone_number=models.IntegerField()
    mat_receipt_num=models.IntegerField(verbose_name='Matriculation receipt NO')
    mat_receipt_num_date=models.DateField('Date isued ',auto_now_add=False, auto_now=False, null=True)
    convocation_gown_receipt_num=models.IntegerField(verbose_name='Convocation gown receipt NO', null=True)
    convocation_gown_receipt_num_date=models.DateField('Date issued ',auto_now_add=False, auto_now=False, null=True)
    alumini_receipt_num=models.IntegerField(verbose_name='Alumini receipt NO')
    alumini_receipt_num_date=models.DateField('Date issued ',auto_now_add=False, auto_now=False)
    school_fees_receipt_year_1=models.IntegerField(verbose_name='School fees (year-1) receipt NO')
    school_fees_receipt_year_1_date=models.DateField('Date issued ',auto_now_add=False, auto_now=False)
    school_fees_receipt_year_2=models.IntegerField(verbose_name='School fees (year-2) receipt NO')
    school_fees_receipt_year_2_date=models.DateField('Date issued ',auto_now_add=False, auto_now=False)
    enterpreneur_receipt_num=models.IntegerField(verbose_name='Enterpreneur receipt NO')
    enterpreneur_receipt_num_date=models.DateField('Date issued ',auto_now_add=False, auto_now=False)
    certificate_processing_fee_receipt=models.IntegerField(verbose_name='Enterpreneur receipt NO', null=True)
    certificate_processing_fee_receipt_date=models.DateField('Date issued ',auto_now_add=False, auto_now=False, null=True)
    date_posted=models.DateField(auto_now_add=True, auto_now=False)
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    # student affairs review 
    student_affair_review=models.CharField(default='pending',max_length=15, null=True)
    student_affair_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    sa_approved_by=models.CharField(max_length=50,null=True, blank=True)
    student_affair_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # student union government review 
    sug_review=models.CharField(default='pending',max_length=15, null=True)
    sug_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    sug_approved_by=models.CharField(max_length=50, null=True, blank=True)
    sug_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # chief liberian review 
    chief_liberian_review=models.CharField(default='pending',max_length=15, null=True)
    chief_liberian_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    liberian_approved_by=models.CharField(max_length=50, null=True, blank=True)
    chief_liberian_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # sport officer review 
    sport_officer_review=models.CharField(default='pending',max_length=15, null=True)
    sport_officer_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    sport_approved_by=models.CharField(max_length=50, null=True, blank=True)
    sport_officer_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # principal house keeper review (NDDC)
    nddc_hostel_review=models.CharField(default='pending',max_length=15, null=True)
    nddc_hostel_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    nddc_hostel_approved_by=models.CharField(max_length=50, null=True, blank=True)
    nddc_hostel_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # principal house keeper review (noble)
    noble_hostel_review=models.CharField(default='pending',max_length=15, null=True)
    noble_hostel_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    noble_hostel_approved_by=models.CharField(max_length=50, null=True, blank=True)
    noble_hostel_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # principal house keeper review (boy's hostel)
    boys_hostel_review=models.CharField(default='pending',max_length=15, null=True)
    boys_hostel_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    boys_hostel_approved_by=models.CharField(max_length=50, null=True, blank=True)
    sport_officer_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # principal house keeper review (PTDF wing-A)
    ptdf_wing_a_review=models.CharField(default='pending',max_length=15, null=True)
    ptdf_wing_a_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    ptdf_wing_a_approved_by=models.CharField(max_length=50, null=True, blank=True)
    ptdf_wing_a_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    # principal house keeper review (PTDF wing-B)
    ptdf_wing_b_review=models.CharField(default='pending',max_length=15, null=True)
    ptdf_wing_b_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    ptdf_wing_b_approved_by=models.CharField(max_length=50, null=True, blank=True)
    ptdf_wing_b_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)
    #HOD review 
    hod_review=models.CharField(default='pending',max_length=15, blank=True, null=True)
    hod_comment=models.TextField(verbose_name='comment', null=True, blank=True)
    hod_approved_by=models.CharField(max_length=50, null=True, blank=True)
    hod_approval_date=models.DateField('Date of approval',auto_now_add=False, auto_now=False, null=True, blank=True)