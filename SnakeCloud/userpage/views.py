from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def userpage(request, username):
    return render(request, 'user_profile/profile_overview.html', {'userpage': username})

