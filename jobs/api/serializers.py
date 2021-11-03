from rest_framework import serializers
from jobs.models import JobOffer, Student, Course, Faculty, Attendance, Students_zooms, Zooms

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ZoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zooms
        fields = '__all__'

class Students_zoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students_zooms
        fields = '__all__'





