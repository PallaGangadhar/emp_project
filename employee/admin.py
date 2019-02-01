from django.contrib import admin
from employee.models import department, employee, salary, leave, project

admin.site.register(department)
admin.site.register(employee)
admin.site.register(salary)
admin.site.register(leave)
admin.site.register(project)
