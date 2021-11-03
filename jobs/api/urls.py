from django.urls import path
from jobs.api import views

urlpatterns = [
    path('jobs/', views.ListView.as_view(), name='list'),
    path('jobs/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('faculties/<int:pk>/', views.FacultyDetailView.as_view(), name='faculty_detail'),
    path('faculty/', views.FacultyListView.as_view(), name='faculties'),
    path('course/', views.CourseListView.as_view(), name='course'),
    path('student/', views.StudentListView.as_view(), name='student'),
    path('attendance/', views.AttendanceListView.as_view(), name='attendance'),
    path('students_zooms/', views.AttendanceListView.as_view(), name='students_zooms'),
    path('zooms/', views.AttendanceListView.as_view(), name='zooms'),
]

