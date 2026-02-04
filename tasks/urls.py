from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.home,name='home'),
    path('dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('employee/<str:pk>/',views.employee_dashboard,name='employee'),
    path('assigntask',views.assign_task,name='assign_task'),
    path('update_status/<str:pk>/',views.update_task_status,name='update_status'),
    path('department_dashboard/<str:dept>/',views.department_dashboard,name='department')
]