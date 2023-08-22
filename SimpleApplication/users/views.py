from django.shortcuts import render, HttpResponse, Http404
from new_user.models import NewUser


def users_detail(request):
    users = NewUser.objects.all()
    if len(users) <= 0:
        return HttpResponse("Required atleast one user to form the table")
    return render(request, "users/all_users_detail.html", {'user': users})


def get_user(request, id):
    try:
        user = NewUser.objects.get(pk=id)
    except NewUser.DoesNotExist:
        return HttpResponse(f"New User - {id} does not exist")
    return render(request, "users/user_detail.html", {'user': user})
