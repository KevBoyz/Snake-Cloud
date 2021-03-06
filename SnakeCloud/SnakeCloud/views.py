from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def root(request):
    return render(request, 'main/home.html')
