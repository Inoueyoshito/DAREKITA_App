from jobs.models import Faculty
from jobs.models import Course
from jobs.models import Student
from jobs.models import Attendance
from jobs.models import Students_zooms
from jobs.models import Zooms
from django.contrib import admin


admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Students_zooms)
admin.site.register(Zooms)



