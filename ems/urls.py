"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from employee import views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('home/', views.logout, name='logout'),
    path('departments/', views.departments, name='department_list'),
    path('employees/', views.employees, name='employees_list'),
    path('assign_projects/', views.projects, name='projects'),
    path('profile/', views.profile, name='profile'),
    #path('leave_request/', views.leaves, name='leaves'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('about_us/', views.about_us, name='about_us'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
