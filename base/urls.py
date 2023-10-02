from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('student/signup/', views.studentsignup, name='student-signup'),
    path('student/profile/create/', views.StudentProfileCreate.as_view(), name='student-profile'),
    path('staff/profile/', views.StaffProflieCreate.as_view(), name='staff-profile'),
    path('student/login/', views.studentlogin, name='student-login'),
    path('staff/login/', views.stafflogin, name='staff-login'),
    path('staff/dashboard/', views.staffdashboard, name='staff-dashboard'),
    path('student/dashboard/', views.studentdashboard, name='student-dashboard'),
    path('logout/', LogoutView.as_view(template_name='home.html'), name='user-logout'),

    path('student/query/',views.search, name='search'),
    path('clearance/form/', views.ClearanceFormView.as_view(), name='clearance-form'),
    path('students/form/<int:pk>', views.ClearanceFormDetailView.as_view(), name='clearance-form-detail'),
    path('students/form/delete/<int:pk>', views.ClearanceFormDeleteView.as_view(), name='clearance-form-delete'),
    
    path('studentaffair/approve/<int:pk>', views.StudentAffairApproveView.as_view(), name='studentaffair-approve'),
    path('studentaffair/disapprove/<int:pk>', views.StudentAffairDisapproveView.as_view(), name='studentaffair-disapprove'),
    path('studentaffair/review/', views.StudentAffairPending.as_view(), name='studentaffair-review'),

    path('studentunion/approve/<int:pk>', views.StudentUnionApproveView.as_view(), name='studentunion-approve'),
    path('studentunion/disapprove/<int:pk>', views.StudentUnionDisapproveView.as_view(), name='studentunion-disapprove'),
    path('studentunion/review/', views.StudentUnionPending.as_view(), name='studentunion-review'),

    path('library/approve/<int:pk>', views.LibraryApproveView.as_view(), name='library-approve'),
    path('library/disapprove/<int:pk>', views.LibraryDisapproveView.as_view(), name='library-disapprove'),
    path('library/review/', views.LibraryPending.as_view(), name='library-review'),
    
    path('sportsoffice/approve/<int:pk>', views.SportsOfficeApproveView.as_view(), name='sportsoffice-approve'),
    path('sportsoffice/disapprove/<int:pk>', views.SportsOfficeDisapproveView.as_view(), name='sportsoffice-disapprove'),
    path('sportsoffice/review/', views.SportsOfficePending.as_view(), name='sportsoffice-review'),
    
    path('nddc-hostel/approve/<int:pk>', views.NddcApproveView.as_view(), name='nddchostel-approve'),
    path('nddc-hostel/disapprove/<int:pk>', views.NddcDisapproveView.as_view(), name='nddc-hostel-disapprove'),
    path('nddc-hostel/review/', views.NddcPending.as_view(), name='nddchostel-review'),
    
    path('noble-hostel/approve/<int:pk>', views.NobleApproveView.as_view(), name='noblehostel-approve'),
    path('noble-hostel/disapprove/<int:pk>', views.NobleDisapproveView.as_view(), name='noble-hostel-disapprove'),
    path('noble-hostel/review/', views.NoblePending.as_view(), name='noblehostel-review'),
    
    path('wing-b-hostel/approve/<int:pk>', views.WingbApproveView.as_view(), name='wing-b-hostel-approve'),
    path('wing-b-hostel/disapprove/<int:pk>', views.WingbDisapproveView.as_view(), name='wing-b-hostel-disapprove'),
    path('wing-b-hostel/review/', views.WingbPending.as_view(), name='wing-b-hostel-review'),
    
    path('wing-a-hostel/approve/<int:pk>', views.WingaApproveView.as_view(), name='wing-a-hostel-approve'),
    path('wing-a-hostel/disapprove/<int:pk>', views.WingaDisapproveView.as_view(), name='wing-a-hostel-disapprove'),
    path('wing-a-hostel/review/', views.WingaPending.as_view(), name='wing-a-hostel-review'),
    
    path('male-hostel/approve/<int:pk>', views.MaleHostelsApproveView.as_view(), name='male-hostel-approve'),
    path('male-hostel/disapprove/<int:pk>', views.MaleHostelsDisapproveView.as_view(), name='male-hostel-disapprove'),
    path('male-hostel/review/', views.MaleHostelsPending.as_view(), name='male-hostel-review'),
    
    path('csit-hod/approve/<int:pk>', views.CsitHodApproveView.as_view(), name='csit-hod-approve'),
    path('csit-hod/disapprove/<int:pk>', views.CsitHodDisapproveView.as_view(), name='csit-hod-disapprove'),
    path('csit-hod/review/', views.CsitHodPendingREview.as_view(), name='csit-hod-review'),
 
    path('mec-hod/approve/<int:pk>', views.MecHodApproveView.as_view(), name='mec-hod-approve'),
    path('mec-hod/disapprove/<int:pk>', views.MecHodDisapproveView.as_view(), name='mec-hod-disapprove'),
    path('mec-hod/review/', views.MecHodPendingREview.as_view(), name='mec-hod-review'),
       
    path('eed-hod/approve/<int:pk>', views.EedHodApproveView.as_view(), name='eed-hod-approve'),
    path('eed-hod/disapprove/<int:pk>', views.EedHodDisapproveView.as_view(), name='eed-hod-disapprove'),
    path('eed-hod/review/', views.EedHodPendingREview.as_view(), name='eed-hod-review'),
    
    path('safety-hod/approve/<int:pk>', views.SafetyHodApproveView.as_view(), name='safety-hod-approve'),
    path('safety-hod/disapprove/<int:pk>', views.SafetyHodDisapproveView.as_view(), name='safety-hod-disapprove'),
    path('safety-hod/review/', views.SafetyHodPendingREview.as_view(), name='safety-hod-review'),
    
    path('environ-hod/approve/<int:pk>', views.EnvironHodApproveView.as_view(), name='environ-hod-approve'),
    path('environ-hod/disapprove/<int:pk>', views.EnvironHodDisapproveView.as_view(), name='environ-hod-disapprove'),
    path('environ-hod/review/', views.EnvironHodPendingREview.as_view(), name='environ-hod-review'),
    
    path('mpre-hod/approve/<int:pk>', views.MpreHodApproveView.as_view(), name='mpre-hod-approve'),
    path('mpre-hod/disapprove/<int:pk>', views.MpreHodDisapproveView.as_view(), name='mpre-hod-disapprove'),
    path('mpre-hod/review/', views.MpreHodPendingREview.as_view(), name='mpre-hod-review'),
    
    path('pngpd-hod/approve/<int:pk>', views.PngpdHodApproveView.as_view(), name='pngpd-hod-approve'),
    path('pngpd-hod/disapprove/<int:pk>', views.PngpdHodDisapproveView.as_view(), name='pngpd-hod-disapprove'),
    path('pngpd-hod/review/', views.PngpdHodPendingREview.as_view(), name='pngpd-hod-review'),
    
    path('peg-hod/approve/<int:pk>', views.PegHodApproveView.as_view(), name='peg-hod-approve'),
    path('peg-hod/disapprove/<int:pk>', views.PegHodDisapproveView.as_view(), name='peg-hod-disapprove'),
    path('peg-hod/review/', views.PegHodPendingREview.as_view(), name='peg-hod-review'),
    
    path('pmbs-hod/approve/<int:pk>', views.PmbsHodApproveView.as_view(), name='pmbs-hod-approve'),
    path('pmbs-hod/disapprove/<int:pk>', views.PmbsHodDisapproveView.as_view(), name='pmbs-hod-disapprove'),
    path('pmbs-hod/review/', views.PmbsHodPendingREview.as_view(), name='pmbs-hod-review'),
    
    path('slt-hod/approve/<int:pk>', views.SltHodApproveView.as_view(), name='slt-hod-approve'),
    path('slt-hod/disapprove/<int:pk>', views.SltHodDisapproveView.as_view(), name='slt-hod-disapprove'),
    path('slt-hod/review/', views.SltHodPendingREview.as_view(), name='slt-hod-review'),
    
    path('woet-hod/approve/<int:pk>', views.WoetHodApproveView.as_view(), name='woet-hod-approve'),
    path('woet-hod/disapprove/<int:pk>', views.WoetHodDisapproveView.as_view(), name='woet-hod-disapprove'),
    path('woet-hod/review/', views.WoetHodPendingREview.as_view(), name='woet-hod-review'),
    
    path('computer-eng-hod/approve/<int:pk>', views.ComputerEngHodApproveView.as_view(), name='computer-eng-hod-approve'),
    path('computer-eng-hod/disapprove/<int:pk>', views.ComputerEngHodDisapproveView.as_view(), name='computer-eng-hod-disapprove'),
    path('computer-eng-hod/review/', views.ComputerEngHodPendingREview.as_view(), name='computer-eng-hod-review'),
    
    path('mect-hod/approve/<int:pk>', views.MectHodApproveView.as_view(), name='mect-hod-approve'),
    path('mect-hod/disapprove/<int:pk>', views.MectHodDisapproveView.as_view(), name='mect-hod-disapprove'),
    path('mect-hod/review/', views.MectHodPendingREview.as_view(), name='mect-hod-review'),
]