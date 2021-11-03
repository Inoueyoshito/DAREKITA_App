from django.db import models

class JobOffer(models.Model):
    company_name = models.CharField('会社名',max_length=100)
    company_email = models.EmailField()
    jobs_title = models.CharField(max_length=100)
    jobs_description = models.TextField()
    salary = models.PositiveIntegerField()
    prefectures = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.company_name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.number

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=100)
    attendance_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.location_type

class Zooms(models.Model):
    number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.number

class Students_zooms(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    zooms = models.ForeignKey(Zooms, on_delete=models.CASCADE)
    row3 = models.CharField(max_length=100)
    row2 = models.CharField(max_length=100)
    def __str__(self):
        return self.row3

# class Zooms(models.Model):
#     number = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.number









# faculty = Faculty(name='高等部')
# faculty.save()

# all_faculties = Faculty.objects.all()
# print(all_faculties)

# one_faculty = Faculty.objects.get(pk=1)
# # print(one_faculty.name)
# one_faculty.name = "aa"
# one_faculty.save()
# print(one_faculty.name)
# one_faculty.delete()

