from django.contrib import admin
from employee.models import department, employee, leave, project
from django.contrib.auth.models import User,Group

class employee_list(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','gender','email','date_of_joining','phone_no','city','skills','image_tag','dept')

class project_list(admin.ModelAdmin):
    list_display = ('project_name','emp','dept','project_technology','project_start_date','project_end_date')
    
class leave_request(admin.ModelAdmin):
    list_display = ('dept', 'emp', 'leave_reason', 'leave_time', 'leave_date')
    
admin.site.register(department)
admin.site.register(employee, employee_list)
# admin.site.register(salary)
admin.site.register(leave, leave_request)
admin.site.register(project, project_list)
admin.site.unregister(Group)

admin.site.site_header = ("Employee Management System")
admin.site.site_title = ("EMS")
admin.site.index_title = ("Administraion")