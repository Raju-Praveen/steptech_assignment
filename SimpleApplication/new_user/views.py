from django.shortcuts import render, HttpResponse
from .models import NewUser


def create_new_user(request):
    return render(request, "new_user/create_new_user.html", {})


def create_user(request):
    new_id = request.POST.get('userid')
    new_name = request.POST.get('username')
    new_email = request.POST.get('useremail')
    new_role = request.POST.get('userrole')
    new_user = NewUser(uid=new_id,
                       uname=new_name,
                       uemail=new_email,
                       urole=new_role,
                       )
    new_user.save()
    return HttpResponse("Successfully saved...")
