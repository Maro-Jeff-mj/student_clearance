from .models import ClearanceForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import UpdateView , ListView
import datetime

global Department

Department=(
    ('Computer Science and Information Technology'),
    ('Mechanical Engineering Technology'),
    ('Electrical Engineering'),
    ('Industrial Safety'),
    ('Environmentl Technology'),
    ('Mineral and Petroleum Resources'),
    ('Petroleum and Natural Gas Processing Technology'),
    ('Petroleum Engineering and Geoscience'),
    ('Petroleum Marketing and Business Studies'),
    ('Science Laboratory Technology'),
    ('Welding Engineering and Offshore Technology'),
    ('Computer Engineering Technoloy'),
    ('Mechatronics')
)
    
class HodBaseTemplate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= ClearanceForm
    template_name='clearance-approval.html'
    fields=['hod_comment']
    date_qs= str(datetime.date.today())
    status='approved'
    admin=''
    x=''
    def form_valid(self, form):
        form.instance.hod_review = self.status
        form.instance.hod_approved_by= str(self.request.user)
        form.instance.hod_approval_date= self.date_qs
        return super().form_valid(form)
    
    def test_func(self):
        get_student_data= self.get_object()
        if get_student_data.department == self.x:
            if self.request.user.username == self.admin:
                return True
        return False
    
class BasePending(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model=ClearanceForm
    context_object_name='objects'
    template_name='review-portal-template/all-hod-template.html'
    paginate_by=1
    admin=''

    def test_func(self):
        if self.request.user.username == self.admin:
            return True
        return False 
    
class HodBasePending(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model=ClearanceForm
    context_object_name='objects'
    template_name='review-portal-template/all-hod-template.html'
    paginate_by=1
    admin=''
    x= Department[0]
    def test_func(self):
        if self.request.user.username == self.admin:
            return True
        return False 
    
    def get_queryset(self):
        return ClearanceForm.objects.filter(hod_review='pending', department=self.x)

class BaseReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= ClearanceForm
    template_name='clearance-approval.html'
    date_qs= str(datetime.date.today())
    status='approved'
    admin=''
    def test_func(self):
        if self.request.user.username == self.admin:
            return True
        return False
