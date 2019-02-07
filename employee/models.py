from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
# Create your models here.
from django.core.exceptions import ValidationError


class department(models.Model):
    dept_name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Department'
    def __str__(self):
        return self.dept_name


class employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
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
    salary = models.IntegerField(default=0)
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="120" height="120" />' % (self.profile_image))
    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Employee'

class leave(models.Model):
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    emp = models.ForeignKey(employee, on_delete=models.CASCADE)
    leave_reason = models.CharField(max_length=128,blank=False)
    leave_date = models.DateField(default=0,blank=True)
    leave_time = models.CharField(max_length=128,default=0)
    class Meta:
        verbose_name_plural = 'Leave'

    def __str__(self):
        return self.leave_reason

class project(models.Model):
    dept = models.ForeignKey(department, on_delete=models.CASCADE)
    emp = models.ForeignKey(employee, on_delete=models.CASCADE)
    
    project_name = models.CharField(max_length=128, blank=False)
    project_start_date = models.DateField(blank=False)
    project_end_date = models.DateField(blank=False)
    project_technology = models.CharField(max_length=128, blank=False)

    class Meta:
        verbose_name_plural = 'Project'
    
    def __str__(self):
        return self.project_name


    def clean(self):
        """ warn if selected city is not in selected country """
        if (self.dept and self.emp and self.emp.dept.id != self.dept.id):
            raise ValidationError(message='%(emp_name)s is not in %(dept_name)s',
                                  code='wrong_country',
                                  params=dict(emp_name=self.emp.first_name, 
                                              dept_name=self.dept.dept_name))
