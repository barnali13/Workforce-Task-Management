from django.shortcuts import render,redirect
from .forms import *
from .models import Task
from user.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user = request.user

    # ---------------- GLOBAL STATS ----------------
    total_users = User.objects.count() - 2
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status="COMPLETED").count()

    success_rate = (
        round((completed_tasks / total_tasks) * 100)
        if total_tasks > 0 else 0
    )

    # ---------------- ALL DEPARTMENTS ----------------
    profiles = UserProfile.objects.all()

    # Get unique departments (excluding NULL/empty)
    departments = profiles.exclude(dept__isnull=True).exclude(dept='').values_list('dept', flat=True).distinct()

    department_data = []

    for dept_name in departments:
      
        # Get all tasks assigned to users in this department
        dept_tasks = Task.objects.filter(assigned_to__dept=dept_name)

        total_dept_tasks = dept_tasks.count()
        completed = dept_tasks.filter(status="COMPLETED").count()
        pending = dept_tasks.filter(status="PENDING").count()

        completion_rate = (
            round((completed / total_dept_tasks) * 100)
            if total_dept_tasks > 0 else 0
        )

        department_data.append({
            'name': dept_name,
            'total_tasks': total_dept_tasks,
            'completedd': completed,
            'pendingg': pending,
            'completion_rate': completion_rate
        })
   

    context = {
        'role': user.userprofile.role,
        'department':user.userprofile.dept,
        'total_users': total_users,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'success_rate': success_rate,
        'departments': department_data,
        'pk':user.userprofile.id
        
    }
  


    return render(request, 'tasks/main_dashboard.html', context)
def admin_dashboard(request,pk):
    tasks=Task.objects.all().order_by('-updated_at')
    task_total=tasks.count()
    pending=tasks.filter(status="PENDING").count()
    in_progress=tasks.filter(status="IN PROGRESS").count()
    completed=tasks.filter(status="COMPLETED").count()
    user=UserProfile.objects.get(id=pk)
    context={
        'tasks':tasks,
        'total_task':task_total,
        'user':user,
        'pending':pending,
        'in_progress':in_progress,
        'completed':completed,
        'pk':pk
    }
    return render(request,'tasks/admin_dashboard.html',context)
def employee_dashboard(request,pk):
    user=UserProfile.objects.get(id=pk)
    tasks=user.task_set.all()
    task_total=tasks.count()
    pending=tasks.filter(status="PENDING").count()
    in_progress=tasks.filter(status="IN PROGRESS").count()
    completed=tasks.filter(status="COMPLETED").count()
    context={
        'user':user,
        'tasks':tasks,
        'total_task':task_total,
        'pending':pending,
        'in_progress':in_progress,
        'completed':completed

    }
    return render(request,'tasks/employee_dashboard.html',context)
def assign_task(request,pk):
    form=TaskForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard',pk=pk)
    context={
        'form':form,
        'mode':"create"

    }
    return render(request,'tasks/task_form.html',context)
def update_task_status(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskStatusUpdateForm(instance=task)
    if request.method == "POST":
        form=TaskStatusUpdateForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,
             "mode":"update"
             }
    return render(request,'tasks/task_form.html',context)

