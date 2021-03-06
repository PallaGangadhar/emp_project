from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from employee import views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('departments/', views.departments, name='department_list'),
    path('employees/', views.employees, name='employees_list'),
    path('manager/', views.manager, name='manager_list'),
    path('edit/<eid>', views.edit, name='edit'),
    path('delete/<eid>', views.delete_employee, name='delete'),
    path('assign_projects/', views.projects, name='projects'),
    path('profile/', views.profile, name='profile'),
    #path('leave_request/', views.leaves, name='leaves'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('leaves/', views.show_leaves, name='show_leaves'),
    path('about_us/', views.about_us, name='about_us'),
    path('approve/<lid>', views.approve, name='approve'),
    path('deny/<lid>', views.deny, name='deny'),
    path('all_project/', views.all_projects, name='all_projects'),
    # path('add_project/', views.add_project, name='add_project'),
    path('fill_by_dept/', views.fill_by_dept, name='fill'),
    path('employee_register/', views.employee_register, name='employee_register'),
    path('help_desk/', views.help_desk, name='help_desk'),
    
    
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
