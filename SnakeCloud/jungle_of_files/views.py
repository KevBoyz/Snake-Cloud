from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def dashboard(request):
    return render(request, 'jungle/dashboard.html')


@login_required(login_url='/auth/login/')
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        return HttpResponse(f'{title} {description}')
    elif request.method == 'GET':
        return render(request, 'jungle/upload.html')

