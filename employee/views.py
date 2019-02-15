from django.shortcuts import render, redirect
from employee.models import department, employee, project, leave
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    uname = request.session.get('uname')
    e2 = employee.objects.filter(email=uname)
    emp = employee.objects.all()[:1]
    return render(request, 'employee/index.html', {'emp': e2, 'emp1': emp})


def departments(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        departments = department.objects.filter(dept_name__istartswith=name)
       
        dict1 = {}
        for d in departments:
            if d.dept_name not in dict1:
                c = 0
                c = employee.objects.filter(dept_id=d.id).count()
                dict1[d.dept_name] = c
    else:
        departments = department.objects.all()
        emp = employee.objects.all()
        dict1 = {}
        for d in departments:
            if d.dept_name not in dict1:
                c = 0
                c = employee.objects.filter(dept_id=d.id).count()
                dict1[d.dept_name] = c
    return render(request, 'employee/department_list.html', {'dict1': dict1})


def employees(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        emp = employee.objects.filter(
            Q(first_name__contains=name) | Q(last_name__istartswith=name) | Q(dept__dept_name__istartswith=name))
        context_dict = {'employees': emp}
    else:
        employee_list = employee.objects.order_by('-date_of_joining')
        context_dict = {'employees': employee_list}
    return render(request, 'employee/employee_list.html', context_dict)


def login(request):
    emp = employee.objects.all()
    uname = ''
    if request.method == 'POST':
        uname = request.POST.get('email')
        password = request.POST.get('password')
        for e in emp:
            if e.email == uname and e.password == password:
                request.session['role'] = e.role
                request.session['dept'] = e.dept_id
                request.session['uname'] = e.email
                request.session['fname'] = e.first_name
                request.session['lname'] = e.last_name
                request.session['eid'] = e.id
                request.session['image'] = str(e.profile_image)
                return redirect('index')
    
    return render(request, 'employee/login.html', {'e': emp})


def profile(request):
    fname = request.session.get('uname')
    e2 = employee.objects.filter(email=fname)
    return render(request, 'employee/profile.html', {'emp': e2})


def projects(request):
    project_list = project.objects.all()
    eid = request.session.get('eid')
    p1 = ''
    for p in project_list:
        if p.emp_id == eid:
            p1 = project.objects.filter(emp_id=eid)
    context_dict = {'projects': p1}
    return render(request, 'employee/project_list.html', context_dict)

# def leaves(request):
#     eid = request.session.get('eid')
#     emp = employee.objects.get(id=eid)
#     if request.method == "POST":
#         l = leave()
#         l.dept_id = request.POST.get('dept_id')
#         l.emp_id = request.POST.get('emp_id')
#         l.leave_date = request.POST.get('leave_date')
#         l.leave_time = request.POST.get('leave_time')
#         l.leave_reason = request.POST.get('leave_reason')
#         l.save()
#         return redirect('leaves')
#     return render(request, 'employee/leaves.html',{'dname':emp.dept ,'ename': emp.first_name,'dept_id':emp.dept_id,'emp_id':emp.id})


def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('index')


def leave_request(request):
    eid = request.session.get('eid')
    emp = employee.objects.get(id=eid)
    emp_leave = leave.objects.filter(emp=eid)
    if request.method == "POST":
    
        l = leave()
        l.dept_id = request.POST.get('dept_id')
        l.emp_id = request.POST.get('emp_id')
        l.leave_date = request.POST.get('leave_date')
        l.leave_time = request.POST.get('leave_time')
        l.leave_reason = request.POST.get('leave_reason')
      
        l.save()

        
    return render(request, 'employee/leave_request.html', {'dname': emp.dept, 'ename': emp.first_name, 'dept_id': emp.dept_id, 'emp_id': emp.id,'emp_leave':emp_leave})


def about_us(request):
    return render(request, 'employee/about-us.html', {})


def edit(request, eid):
    emp = employee.objects.filter(id=eid)
    if request.method == 'POST':
        e = employee.objects.get(id=eid)
        e.first_name = request.POST.get('fname')
        e.last_name = request.POST.get('lname')
        e.phone_no = request.POST.get('phone_no')
        e.address = request.POST.get('address')
        e.city = request.POST.get('city')
        e.designation = request.POST.get('designation')
        e.skills = request.POST.get('skills')
        e.experience = request.POST.get('experience')
        if request.FILES.get('profile_image'):
            e.profile_image = request.FILES.get('profile_image')

        e.salary = request.POST.get('salary')
        e.save()
        return redirect('employees_list')
    return render(request, 'employee/edit.html', {'emp': emp})


def delete_employee(request, eid):
    e = employee.objects.get(id=eid)
    e.delete()
    return redirect('employees_list')


def show_leaves(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        leaves = leave.objects.filter(dept__dept_name__istartswith=name)
        print(leaves)
        context_dict = {'leaves': leaves}
    else:
        leaves = leave.objects.all().order_by('-leave_date')
        context_dict = {'leaves': leaves}
    return render(request, 'employee/show_leaves.html', context_dict)


def approve(request, lid):
    l = leave.objects.filter(id=lid)
    if request.method == "POST":
        le = leave.objects.get(id=lid)
        le.leave_status = 'Approve'
        le.save()
        return redirect('show_leaves')
    return render(request, 'employee/show_leaves.html')


def deny(request, lid):
    l = leave.objects.filter(id=lid)
    if request.method == "POST":
        le = leave.objects.get(id=lid)
        le.leave_status = 'Deny'
        le.save()
        return redirect('show_leaves')
    return render(request, 'employee/show_leaves.html')


def all_projects(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        project_list = project.objects.filter(project_name__istartswith=name)
        context_dict = {'projects': project_list}
    else:
        project_list = project.objects.all()
        context_dict = {'projects': project_list}
    return render(request, 'employee/all_projects.html', context_dict)


def fill_by_dept(request):
    dept = department.objects.all()
    dept_id = request.GET.get('dept_id')
    
    emp = employee.objects.filter(dept=dept_id)
    for e in emp:
        print(e.first_name)
    return render(request,'employee/add_project.html',{'dept':dept,'emp':emp})

# def add_project(request):
#     # if request.method == 'POST':
#     dept = department.objects.all()
#     emp = employee.objects.all()
#     return render(request,'employee/add_project.html',{'emp':emp,'dept':dept})

def employee_register(request):
    dept = department.objects.all()
    if request.method == 'POST':
        e = employee()
        e.dept_id = request.POST.get('dept')
        e.first_name = request.POST.get('fname')
        e.last_name = request.POST.get('lname')
        e.gender = request.POST.get('gender')
        e.date_of_birth = request.POST.get('dob')
        e.email = request.POST.get('email')
        e.password = request.POST.get('password')
        e.phone_no = request.POST.get('phone_no')
        e.address = request.POST.get('address')
        e.city = request.POST.get('city')
        e.qualification = request.POST.get('qualification')
        e.designation = request.POST.get('designation')
        e.skills = request.POST.get('skills')
        e.experience = request.POST.get('experience')
        e.date_of_joining = request.POST.get('doj')
        if request.FILES.get('profile_image'):
            e.profile_image = request.FILES.get('profile_image')

        e.salary = request.POST.get('salary')
        e.save()
        return redirect('employees_list')
    return render(request,'employee/employee_register.html',{'dept':dept})

def manager(request):
    emp = employee.objects.filter(role='Manager')
    return render(request,'employee/manager_list.html',{'employees':emp})

def help_desk(request):
    return render(request,'employee/help_desk.html', {})
    
def demo(request):
    return render(request,'employee/demo.html', {})
