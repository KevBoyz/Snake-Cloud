from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/auth/login/')
def userpage(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user_profile/profile_overview.html', {'userpage': user})


def users_list(request):
    usrs = User.objects.all()
    return render(request, 'user_profile/users_list.html', {'usrs': usrs})

