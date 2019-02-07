from django.shortcuts import render, redirect
from employee.models import department, employee, project, leave

def index(request):
    uname = request.session.get('uname')
    e2 = employee.objects.filter(email=uname)
    emp = employee.objects.all() [:1]
    return render(request, 'employee/index.html', {'emp':e2,'emp1':emp} )

def departments(request):
    departments = department.objects.all()
    emp = employee.objects.all() 
    dict1={}
    # for d in departments:
    #     if d.dept_name not in dict1:
    #         c = 0
    #         for e in emp:
    #             if d.id == e.dept.id:
    #                 c = c + 1
    #         dict1[d.dept_name] = c
    for d in departments:
        if d.dept_name not in dict1:
            c = 0
            c = employee.objects.filter(dept_id =d.id).count()
            dict1[d.dept_name] = c
    return render(request, 'employee/department_list.html', {'dict1': dict1})

def employees(request):
    employee_list = employee.objects.all()
    context_dict = {'employees':employee_list}
    return render(request, 'employee/employee_list.html', context_dict)

def login(request):
    emp = employee.objects.all()
    uname = ''
    if request.method == 'POST':
        uname = request.POST.get('email')
        password = request.POST.get('password')
        for e in emp:
            if e.email == uname and e.password == password:
                request.session['uname'] = e.email
                request.session['fname'] = e.first_name
                request.session['lname'] = e.last_name  
                request.session['eid'] = e.id
                request.session['image'] = str(e.profile_image)
                
                return redirect('index')
        
    return render(request,'employee/login.html',{'e':emp})


def profile(request):
    fname = request.session.get('uname')
    e2 = employee.objects.filter(email=fname)
    return render(request,'employee/profile.html',{'emp':e2})  

def projects(request):
    project_list = project.objects.all()
    eid = request.session.get('eid')
    p1= ''
    for p in project_list:
        if p.emp_id == eid:
            p1 = project.objects.filter(emp_id=eid)
           
    context_dict = {'projects':p1}
    return render(request, 'employee/project_list.html', context_dict)

def leaves(request):
    eid = request.session.get('eid')
    emp = employee.objects.get(id=eid)
    if request.method == "POST":
        print('jiiii')
        l = leave()
        l.dept_id = request.POST.get('dept_id')
        l.emp_id = request.POST.get('emp_id')
        l.leave_date = request.POST.get('leave_date')
        l.leave_time = request.POST.get('leave_time')
        l.leave_reason = request.POST.get('leave_reason')
        l.save()
        return redirect('leaves')
    return render(request, 'employee/leaves.html',{'dname':emp.dept ,'ename': emp.first_name,'dept_id':emp.dept_id,'emp_id':emp.id})

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]

    return render(request,'employee/index.html')

def leave_request(request):
    eid = request.session.get('eid')
    emp = employee.objects.get(id=eid)
    if request.method == "POST":
        print('jiiii')
        l = leave()
        l.dept_id = request.POST.get('dept_id')
        l.emp_id = request.POST.get('emp_id')
        l.leave_date = request.POST.get('leave_date')
        print(l.leave_date)
        l.leave_time = request.POST.get('leave_time')
        l.leave_reason = request.POST.get('leave_reason')
        l.save()
    
        return redirect('leave_request')
    return render(request, 'employee/leave_request.html',{'dname':emp.dept ,'ename': emp.first_name,'dept_id':emp.dept_id,'emp_id':emp.id})

def about_us(request):
    return render(request,'employee/about-us.html',{})