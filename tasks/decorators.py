from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            user_groups=request.user.groups.values_list('name',flat=True)
            for group in user_groups:
                if group.lower() in [role.lower() for role in allowed_roles]:
                    return view_func(request,*args,**kwargs)
            return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator