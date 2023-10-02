from django import template
from base.models import ClearanceForm
from base.parentviews import Department

register= template.Library()
@register.filter
def get_total(user):
    qs= ClearanceForm.objects.all()
    if qs.exists():
        return ClearanceForm.objects.all().count()
    return f'0'

@register.filter
def student_affair_pending(user):
    qs= ClearanceForm.objects.filter(student_affair_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(student_affair_review="pending").count()
    return f'0'

@register.filter
def student_affair_approved(user):
    qs= ClearanceForm.objects.filter(student_affair_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(student_affair_review="approved").count()
    return f'0'

@register.filter
def student_affair_disapproved(user):
    qs= ClearanceForm.objects.filter(student_affair_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(student_affair_review="disapproved").count()
    return f'0'

@register.filter
def sug_pending(user):
    qs= ClearanceForm.objects.filter(sug_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sug_review="pending").count()
    return f'0'

@register.filter
def sug_approved(user):
    qs= ClearanceForm.objects.filter(sug_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sug_review="approved").count()
    return f'0'

@register.filter
def sug_disapproved(user):
    qs= ClearanceForm.objects.filter(sug_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sug_review="disapproved").count()
    return f'0'

@register.filter
def library_pending(user):
    qs= ClearanceForm.objects.filter(chief_liberian_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(chief_liberian_review="pending").count()
    return f'0'

@register.filter
def library_approved(user):
    qs= ClearanceForm.objects.filter(chief_liberian_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(chief_liberian_review="approved").count()
    return f'0'

@register.filter
def library_disapproved(user):
    qs= ClearanceForm.objects.filter(chief_liberian_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(chief_liberian_review="disapproved").count()
    return f'0'

@register.filter
def sport_pending(user):
    qs= ClearanceForm.objects.filter(sport_officer_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sport_officer_review="pending").count()
    return f'0'

@register.filter
def sport_approved(user):
    qs= ClearanceForm.objects.filter(sport_officer_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sport_officer_review="approved").count()
    return f'0'

@register.filter
def sport_disapproved(user):
    qs= ClearanceForm.objects.filter(sport_officer_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sport_officer_review="disapproved").count()
    return f'0'

@register.filter
def total_female(user):
    qs= ClearanceForm.objects.filter(sex='Female')
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female').count()
    return f'0'

@register.filter
def total_male(user):
    qs= ClearanceForm.objects.filter(sex='Male')
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Male').count()
    return f'0'

@register.filter
def nddc_pending(user):
    qs= ClearanceForm.objects.filter(sex='Female', nddc_hostel_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', nddc_hostel_review="pending").count()
    return f'0'

@register.filter
def nddc_approved(user):
    qs= ClearanceForm.objects.filter(sex='Female', nddc_hostel_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', nddc_hostel_review="approved").count()
    return f'0'

@register.filter
def nddc_disapproved(user):
    qs= ClearanceForm.objects.filter(sex='Female', nddc_hostel_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', nddc_hostel_review="disapproved").count()
    return f'0'

@register.filter
def noble_pending(user):
    qs= ClearanceForm.objects.filter(sex='Female', noble_hostel_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', noble_hostel_review="pending").count()
    return f'0'

@register.filter
def noble_approved(user):
    qs= ClearanceForm.objects.filter(sex='Female', noble_hostel_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', noble_hostel_review="approved").count()
    return f'0'

@register.filter
def noble_disapproved(user):
    qs= ClearanceForm.objects.filter(sex='Female', noble_hostel_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', noble_hostel_review="disapproved").count()
    return f'0'

@register.filter
def wing_a_pending(user):
    qs= ClearanceForm.objects.filter(sex='Male', ptdf_wing_a_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Male', ptdf_wing_a_review="pending").count()
    return f'0'

@register.filter
def wing_a_approved(user):
    qs= ClearanceForm.objects.filter(sex='Male', ptdf_wing_a_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Male', ptdf_wing_a_review="approved").count()
    return f'0'

@register.filter
def wing_a_disapproved(user):
    qs= ClearanceForm.objects.filter(sex='Male', ptdf_wing_a_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Male', ptdf_wing_a_review="disapproved").count()
    return f'0'

@register.filter
def wing_b_pending(user):
    qs= ClearanceForm.objects.filter(sex='Female', ptdf_wing_b_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', ptdf_wing_b_review="pending").count()
    return f'0'

@register.filter
def wing_b_approved(user):
    qs= ClearanceForm.objects.filter(sex='Female', ptdf_wing_b_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', ptdf_wing_b_review="approved").count()
    return f'0'

@register.filter
def wing_b_disapproved(user):
    qs= ClearanceForm.objects.filter(sex='Female', ptdf_wing_b_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', ptdf_wing_b_review="disapproved").count()
    return f'0'

@register.filter
def boys_hostel_pending(user):
    qs= ClearanceForm.objects.filter(sex='Female', boys_hostel_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', boys_hostel_review="pending").count()
    return f'0'

@register.filter
def boys_hostel_approved(user):
    qs= ClearanceForm.objects.filter(sex='Female', boys_hostel_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', boys_hostel_review="approved").count()
    return f'0'

@register.filter
def boys_hostel_disapproved(user):
    qs= ClearanceForm.objects.filter(sex='Female', boys_hostel_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(sex='Female', boys_hostel_review="disapproved").count()
    return f'0'


@register.filter
def csit_total(user):
    qs= ClearanceForm.objects.filter(department=Department[0])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[0]).count()
    return f'0'

@register.filter
def csit_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[0], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[0], hod_review="pending").count()
    return f'0'

@register.filter
def csit_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[0], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[0], hod_review="approved").count()
    return f'0'

@register.filter
def csit_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[0], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[0], hod_review="disapproved").count()
    return f'0'

@register.filter
def mec_total(user):
    qs= ClearanceForm.objects.filter(department=Department[1])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[1]).count()
    return f'0'

@register.filter
def mec_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[1], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[1], hod_review="pending").count()
    return f'0'

@register.filter
def mec_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[1], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[1], hod_review="approved").count()
    return f'0'

@register.filter
def mec_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[1], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[1], hod_review="disapproved").count()
    return f'0'

@register.filter
def eed_total(user):
    qs= ClearanceForm.objects.filter(department=Department[2])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[2]).count()
    return f'0'

@register.filter
def eed_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[2], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[2], hod_review="pending").count()
    return f'0'

@register.filter
def eed_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[2], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[2], hod_review="approved").count()
    return f'0'

@register.filter
def eed_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[2], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[2], hod_review="disapproved").count()
    return f'0'

@register.filter
def safety_total(user):
    qs= ClearanceForm.objects.filter(department=Department[3])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[3]).count()
    return f'0'

@register.filter
def safety_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[3], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[3], hod_review="pending").count()
    return f'0'

@register.filter
def safety_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[3], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[3], hod_review="approved").count()
    return f'0'

@register.filter
def safety_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[3], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[3], hod_review="disapproved").count()
    return f'0'

@register.filter
def environ_total(user):
    qs= ClearanceForm.objects.filter(department=Department[4])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[4]).count()
    return f'0'

@register.filter
def environ_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[4], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[4], hod_review="pending").count()
    return f'0'

@register.filter
def environ_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[4], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[4], hod_review="approved").count()
    return f'0'

@register.filter
def environ_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[4], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[4], hod_review="disapproved").count()
    return f'0'

@register.filter
def mpre_total(user):
    qs= ClearanceForm.objects.filter(department=Department[5])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[5]).count()
    return f'0'

@register.filter
def mpre_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[5], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[5], hod_review="pending").count()
    return f'0'

@register.filter
def mpre_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[5], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[5], hod_review="approved").count()
    return f'0'

@register.filter
def mpre_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[5], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[5], hod_review="disapproved").count()
    return f'0'

@register.filter
def pngpd_total(user):
    qs= ClearanceForm.objects.filter(department=Department[6])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[6]).count()
    return f'0'

@register.filter
def pngpd_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[6], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[6], hod_review="pending").count()
    return f'0'

@register.filter
def pngpd_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[6], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[6], hod_review="approved").count()
    return f'0'

@register.filter
def pngpd_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[6], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[6], hod_review="disapproved").count()
    return f'0'

@register.filter
def peg_total(user):
    qs= ClearanceForm.objects.filter(department=Department[7])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[7]).count()
    return f'0'

@register.filter
def peg_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[7], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[7], hod_review="pending").count()
    return f'0'

@register.filter
def peg_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[7], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[7], hod_review="approved").count()
    return f'0'

@register.filter
def peg_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[7], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[7], hod_review="disapproved").count()
    return f'0'

@register.filter
def pmbs_total(user):
    qs= ClearanceForm.objects.filter(department=Department[8])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[8]).count()
    return f'0'

@register.filter
def pmbs_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[8], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[8], hod_review="pending").count()
    return f'0'

@register.filter
def pmbs_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[8], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[8], hod_review="approved").count()
    return f'0'

@register.filter
def pmbs_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[8], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[8], hod_review="disapproved").count()
    return f'0'

@register.filter
def slt_total(user):
    qs= ClearanceForm.objects.filter(department=Department[9])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[9]).count()
    return f'0'

@register.filter
def slt_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[9], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[9], hod_review="pending").count()
    return f'0'

@register.filter
def slt_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[9], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[9], hod_review="approved").count()
    return f'0'

@register.filter
def slt_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[9], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[9], hod_review="disapproved").count()
    return f'0'

@register.filter
def woet_total(user):
    qs= ClearanceForm.objects.filter(department=Department[10])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[10]).count()
    return f'0'

@register.filter
def woet_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[10], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[10], hod_review="pending").count()
    return f'0'

@register.filter
def woet_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[10], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[10], hod_review="approved").count()
    return f'0'

@register.filter
def woet_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[10], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[10], hod_review="disapproved").count()
    return f'0'

@register.filter
def computer_eng_total(user):
    qs= ClearanceForm.objects.filter(department=Department[11])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[11]).count()
    return f'0'

@register.filter
def computer_eng_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[11], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[11], hod_review="pending").count()
    return f'0'

@register.filter
def computer_eng_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[11], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[11], hod_review="approved").count()
    return f'0'

@register.filter
def computer_eng_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[11], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[11], hod_review="disapproved").count()
    return f'0'

@register.filter
def mect_total(user):
    qs= ClearanceForm.objects.filter(department=Department[12])
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[12]).count()
    return f'0'

@register.filter
def mect_pending(user):
    qs= ClearanceForm.objects.filter(department=Department[12], hod_review="pending")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[12], hod_review="pending").count()
    return f'0'

@register.filter
def mect_approved(user):
    qs= ClearanceForm.objects.filter(department=Department[12], hod_review="approved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[12], hod_review="approved").count()
    return f'0'

@register.filter
def mect_disapproved(user):
    qs= ClearanceForm.objects.filter(department=Department[12], hod_review="disapproved")
    if qs.exists():
        return ClearanceForm.objects.filter(department=Department[12], hod_review="disapproved").count()
    return f'0'