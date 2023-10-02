from django.contrib import admin
from .models import StudentProfile, StaffProfile, ClearanceForm
# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(StaffProfile)
admin.site.register(ClearanceForm)