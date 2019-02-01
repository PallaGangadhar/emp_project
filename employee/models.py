from django.db import models

# Create your models here.


class department(models.Model):
    dept_name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Department'



class employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    dept = models.ForeignKey(department, on_delete=id)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    date_of_birth = models.DateField(max_length=128, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    date_of_joining = models.DateField(blank=False)
    email = models.EmailField(max_length=128, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    phone_no = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=128, blank=False)
    qualification = models.CharField(max_length=128, blank=False)
    designation = models.CharField(max_length=128, blank=False)
    skills = models.CharField(max_length=128, blank=False)
    experience = models.IntegerField(blank=False)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)

    class Meta:
        verbose_name_plural = 'Employee'

class salary(models.Model):
    dept = models.ForeignKey(department, on_delete=id)
    emp = models.ForeignKey(employee, on_delete=id)
    monthly_salary = models.IntegerField(blank=False)

    class Meta:
        verbose_name_plural = 'Salary'

class leave(models.Model):
    dept = models.ForeignKey(department, on_delete=id)
    emp = models.ForeignKey(employee, on_delete=id)
    leave_reason = models.CharField(max_length=128,blank=False)
    leave_date = models.DateField(blank=False)

    class Meta:
        verbose_name_plural = 'Leave'

class project(models.Model):
    dept = models.ForeignKey(department, on_delete=id)
    emp = models.ForeignKey(employee, on_delete=id)
    project_name = models.CharField(max_length=128, blank=False)
    project_start_date = models.DateField(blank=False)
    project_end_date = models.DateField(blank=False)
    project_technology = models.CharField(max_length=128, blank=False)

    class Meta:
        verbose_name_plural = 'Project'
