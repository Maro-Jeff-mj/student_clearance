from django.shortcuts import redirect, render ,HttpResponse
from django.urls import reverse
from .forms import StudentRegistrationForm,StudentClearanceForm, StudentProfileForm,StaffProfileForm
from django.contrib import messages
from django.views.generic import CreateView, DetailView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import StudentProfile, StaffProfile, ClearanceForm
from django.contrib.auth import authenticate,login,logout
from .parentviews import HodBaseTemplate, BasePending,BaseReview, HodBasePending, Department
# Create your views here.

def home(request):
    return render(request, 'home.html')

def search(request):
    if request.user.is_staff:
        if request.method== 'POST':
            searched= request.POST['searched']
            details= ClearanceForm.objects.filter(surname__contains=searched)
            return render(request, 'search.html',{'details':details})
    return HttpResponse('<h1>No search result </h1>')

def studentsignup(request):
    if request.method=='POST':
        form= StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-login')
    else:
        form= StudentRegistrationForm()
    return render(request, 'student-signup.html', {'form':form})

def studentlogin(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            messages.warning(request, f'Try logging in from the staff portal')
        elif user is not None:
            login(request,user)
            return redirect('student-dashboard')
        else:
            messages.warning(request, f'Invalid login credentials')
    return render(request, 'student-login.html')

def stafflogin(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('staff-dashboard')
        if user is None:
            messages.warning(request, f'Invalid staff login credentials')
        else:
            messages.warning(request, f'Try loggin in from the student portal')
    return render(request,'staff-login.html')

@login_required
def staffdashboard(request):
    if request.user.is_staff==False:
        logout(request)
        return redirect('staff-login')
    return render(request, 'staff-dashboard.html')

@login_required
def studentdashboard(request):
    try:
        val= ClearanceForm.objects.get(posted_by = request.user)
        if request.user.is_staff:
            logout(request)
            return redirect('student-login')
        return render(request, 'student-dashboard.html', {'val':val})
    except:
        if request.user.is_staff:
            logout(request)
            return redirect('student-login')
        return render(request, 'student-dashboard.html')

class StudentProfileCreate(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model= StudentProfile
    template_name='student-profile.html'
    success_url='/student/dashboard/'
    form_class=StudentProfileForm

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user.is_staff:
            return False
        return True

class StaffProflieCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model= StaffProfile
    template_name='staff-profile.html'
    success_url='/staff/dashboard/'
    form_class=StaffProfileForm

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class ClearanceFormView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model= ClearanceForm
    template_name='clearance-form.html'
    form_class= StudentClearanceForm
    success_url='/student/dashboard/'
    
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff :
            return False
        return True

class ClearanceFormDetailView(LoginRequiredMixin,UserPassesTestMixin, DetailView):
    model=ClearanceForm
    template_name='clearance-form-detail.html'

    def test_func(self):
        post= self.get_object()
        if self.request.user.is_staff or self.request.user == post.posted_by :
            return True
        return False
    
class ClearanceFormDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=ClearanceForm
    template_name='clearance-form-delete.html'
    success_url='/student/dashoard/'

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.posted_by :
            return True
        return False

class StudentAffairApproveView(BaseReview):
    success_url='/studentaffair/review/'
    fields=['student_affair_comment']
    admin='studentaffair_23'
    def form_valid(self, form):
        form.instance.student_affair_review = self.status
        form.instance.sa_approved_by= str(self.request.user)
        form.instance.student_affair_approval_date= self.date_qs
        return super().form_valid(form)

class StudentAffairDisapproveView(StudentAffairApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class StudentAffairPending(BasePending):
    template_name='review-portal-template/studentaffair.html'
    admin='studentaffair_23'
    def get_queryset(self):
        return ClearanceForm.objects.filter(student_affair_review='pending')

class StudentUnionApproveView(BaseReview):
    success_url='/studentunion/review/'
    fields=['sug_comment']
    admin='studentunion_23'
    def form_valid(self, form):
        form.instance.sug_review = self.status
        form.instance.sug_approved_by= str(self.request.user)
        form.instance.sug_approval_date= self.date_qs
        return super().form_valid(form)

class StudentUnionDisapproveView(StudentUnionApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class StudentUnionPending(BasePending):
    template_name='review-portal-template/studentunion.html'
    admin='studentunion_23'
    def get_queryset(self):
        return ClearanceForm.objects.filter(sug_review='pending')
    
class LibraryApproveView(BaseReview):
    success_url='/library/review/'
    fields=['chief_liberian_comment']
    admin='liberian_23'
    def form_valid(self, form):
        form.instance.chief_liberian_review = self.status
        form.instance.liberian_approved_by= str(self.request.user)
        form.instance.chief_liberian_approval_date= self.date_qs
        return super().form_valid(form)

class LibraryDisapproveView(LibraryApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class LibraryPending(BasePending):
    template_name='review-portal-template/library.html'
    admin='liberian_23'
    def get_queryset(self):
        return ClearanceForm.objects.filter(chief_liberian_review='pending')

class SportsOfficeApproveView(BaseReview):
    success_url='/sportsoffice/review/'
    fields=['sport_officer_comment']
    admin='sportsoffice_23'
    def form_valid(self, form):
        form.instance.chief_liberian_review = self.status
        form.instance.liberian_approved_by= str(self.request.user)
        form.instance.chief_liberian_approval_date= self.date_qs
        return super().form_valid(form)

class SportsOfficeDisapproveView(SportsOfficeApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class SportsOfficePending(BasePending):
    template_name='review-portal-template/sportsoffice.html'
    admin='sportsoffice_23'
    def get_queryset(self):
        return ClearanceForm.objects.filter(sport_officer_review='pending')
    
class NddcApproveView(BaseReview):
    success_url='/nddc-hostel/review/'
    fields=['nddc_hostel_comment']
    admin='nddc_hostel'
    def form_valid(self, form):
        form.instance.nddc_hostel_review = self.status
        form.instance.nddc_hostel_approved_by= str(self.request.user)
        form.instance.nddc_hostel_approval_date= self.date_qs
        return super().form_valid(form)

class NddcDisapproveView(NddcApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class NddcPending(BasePending):
    template_name='review-portal-template/nddc.html'
    admin='nddc_hostel'
    def get_queryset(self):
        return ClearanceForm.objects.filter(nddc_hostel_review='pending', sex='Female')
    
class NobleApproveView(BaseReview):
    success_url='/noble-hostel/review/'
    fields=['noble_hostel_comment']
    admin='noble_hostel'
    def form_valid(self, form):
        form.instance.noble_hostel_review = self.status
        form.instance.noble_hostel_approved_by= str(self.request.user)
        form.instance.noble_hostel_approval_date= self.date_qs
        return super().form_valid(form)
    
class NobleDisapproveView(NobleApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class NoblePending(BasePending):
    template_name='review-portal-template/noble.html'
    admin='noble_hostel'

    def get_queryset(self):
        return ClearanceForm.objects.filter(noble_hostel_review='pending', sex='Female')
    
class WingbApproveView(BaseReview):
    success_url='/wing-b-hostel/review/'
    fields=['ptdf_wing_b_comment']
    admin='ptdf_wing_b'
    def form_valid(self, form):
        form.instance.ptdf_wing_b_review = self.status
        form.instance.ptdf_wing_b_approved_by= str(self.request.user)
        form.instance.ptdf_wing_b_approval_date= self.date_qs
        return super().form_valid(form)

class WingbDisapproveView(WingbApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class WingbPending(BasePending):
    template_name='review-portal-template/wing-b.html'
    admin='ptdf_wing_b'

    def get_queryset(self):
        return ClearanceForm.objects.filter(ptdf_wing_b_review='pending', sex='Female')
    
class WingaApproveView(BaseReview):
    success_url='/wing-a-hostel/review/'
    fields=['ptdf_wing_a_comment']
    admin='ptdf_wing_a'
    def form_valid(self, form):
        form.instance.ptdf_wing_a_review = self.status
        form.instance.ptdf_wing_a_approved_by= str(self.request.user)
        form.instance.ptdf_wing_a_approval_date= self.date_qs
        return super().form_valid(form)

class WingaDisapproveView(WingaApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class WingaPending(BasePending):
    template_name='review-portal-template/wing-a.html'
    admin='ptdf_wing_a'

    def get_queryset(self):
        return ClearanceForm.objects.filter(ptdf_wing_a_review='pending', sex='Male')
     
class MaleHostelsApproveView(BaseReview):
    success_url='/male-hostel/review/'
    fields=['boys_hostel_comment']
    admin='male_hostel'
    def form_valid(self, form):
        form.instance.boys_hostel_review = self.status
        form.instance.boys_hostel_approved_by= str(self.request.user)
        form.instance.boys_hostel_approval_date= self.date_qs
        return super().form_valid(form)
    
class MaleHostelsDisapproveView(MaleHostelsApproveView):
    template_name='clearance-disapproval.html'
    status='disapproved'

class MaleHostelsPending(BasePending):
    template_name='review-portal-template/wing-a.html'
    admin='male_hostel'

    def get_queryset(self):
        return ClearanceForm.objects.filter(boys_hostel_review='pending', sex='Male')
 
class CsitHodApproveView(HodBaseTemplate):
    admin='csit_hod'
    success_url='/csit-hod/review/'
    x=Department[0]
    
class CsitHodDisapproveView(CsitHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class CsitHodPendingREview(HodBasePending):
    admin='csit_hod'
    
class MecHodApproveView(HodBaseTemplate):
    admin='mec_hod'
    success_url='/mec-hod/review/'
    x=Department[1]
    
class MecHodDisapproveView(MecHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class MecHodPendingREview(HodBasePending):
    admin='mec_hod'
    x=Department[1]
    
class EedHodApproveView(HodBaseTemplate):
    admin='eed_hod'
    success_url='/eed-hod/review/'
    x=Department[2]

class EedHodDisapproveView(EedHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class EedHodPendingREview(HodBasePending):
    admin='mec_hod'
    x=Department[2]

class SafetyHodApproveView(HodBaseTemplate):
    admin='safety_hod'
    success_url='/safety-hod/review/'
    x=Department[3]

class SafetyHodDisapproveView(SafetyHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class SafetyHodPendingREview(HodBasePending):
    admin='safety_hod'
    x=Department[3]
    
class EnvironHodApproveView(HodBaseTemplate):
    admin='environ_hod'
    success_url='/environ-hod/review/'
    x=Department[4]

class EnvironHodDisapproveView(EnvironHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class EnvironHodPendingREview(HodBasePending):
    admin='environ_hod'
    x=Department[4]

class MpreHodApproveView(HodBaseTemplate):
    admin='mpre_hod'
    success_url='/mpre-hod/review/'
    x=Department[5]

class MpreHodDisapproveView(MpreHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class MpreHodPendingREview(HodBasePending):
    admin='mpre_hod'
    x=Department[5]

class PngpdHodApproveView(HodBaseTemplate):
    admin='pngpd_hod'
    success_url='/pngpd-hod/review/'
    x=Department[6]

class PngpdHodDisapproveView(PngpdHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class PngpdHodPendingREview(HodBasePending):
    admin='pngpd_hod'
    x=Department[6]

class PegHodApproveView(HodBaseTemplate):
    admin='peg_hod'
    success_url='/peg-hod/review/'
    x=Department[7]

class PegHodDisapproveView(PegHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class PegHodPendingREview(HodBasePending):
    admin='peg_hod'
    x=Department[7]
    
class PmbsHodApproveView(HodBaseTemplate):
    admin='pmbs_hod'
    success_url='/pmbs-hod/review/'
    x=Department[8]

class PmbsHodDisapproveView(PmbsHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class PmbsHodPendingREview(HodBasePending):
    admin='pmbs_hod'
    x=Department[8]
    
class SltHodApproveView(HodBaseTemplate):
    admin='slt_hod'
    success_url='/slt-hod/review/'
    x=Department[9]

class SltHodDisapproveView(SltHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class SltHodPendingREview(HodBasePending):
    admin='slt_hod'
    x=Department[9]
    
class WoetHodApproveView(HodBaseTemplate):
    admin='woet_hod'
    success_url='/woet-hod/review/'
    x=Department[10]

class WoetHodDisapproveView(WoetHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class WoetHodPendingREview(HodBasePending):
    admin='woet_hod'
    x=Department[10]
    
class ComputerEngHodApproveView(HodBaseTemplate):
    admin='computer_eng_hod'
    success_url='/computer-eng-hod/review/'
    x=Department[11]

class ComputerEngHodDisapproveView(ComputerEngHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class ComputerEngHodPendingREview(HodBasePending):
    admin='computer_eng_hod'
    x=Department[11]
    
class MectHodApproveView(HodBaseTemplate):
    admin='mect_hod'
    success_url='/mect-hod/review/'
    x=Department[12]

class MectHodDisapproveView(MectHodApproveView):
    status='disapproved'
    template_name='clearance-disapproval.html'
    
class MectHodPendingREview(HodBasePending):
    admin='mect_hod'
    x=Department[12]