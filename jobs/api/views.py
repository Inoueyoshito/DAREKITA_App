from rest_framework import generics
from jobs.models import JobOffer, Faculty, Course, Student, Attendance, Students_zooms, Zooms
from jobs.api.serializers import JobOfferSerializer, FacultySerializer, CourseSerializer, StudentSerializer, AttendanceSerializer, Students_zoomsSerializer, ZoomsSerializer


class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by('-id')
    serializer_class = JobOfferSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer

class FacultyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyListView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.order_by('-updated_at')
    serializer_class = CourseSerializer
    

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.order_by('-created_at')
    serializer_class = StudentSerializer

class AttendanceListView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class Students_zoomsListView(generics.ListCreateAPIView):
    queryset = Students_zooms.objects.all()
    serializer_class = Students_zoomsSerializer

class ZoomsListView(generics.ListCreateAPIView):
    queryset = Zooms.objects.all()
    serializer_class = ZoomsSerializer

