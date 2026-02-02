from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('dashboard/<str:pk>/',views.admin_dashboard,name='admin_dashboard'),
    path('employee/<str:pk>/',views.employee_dashboard,name='employee'),
    path('assigntask/<str:pk>',views.assign_task,name='assign_task'),
    path('update_status/<str:pk>/',views.update_task_status,name='update_status')
]