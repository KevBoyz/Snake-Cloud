from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FilePost


@login_required(login_url='/auth/login/')
def dashboard(request):
    return render(request, 'jungle/dashboard.html')


@login_required(login_url='/auth/login/')
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('upload_file')
        try:
            file_upload = FilePost(
                user=request.user,
                title=title,
                description=description,
                file=file
            )
            file_upload.save()
            return redirect('dashboard')
        except Exception as e:
            return HttpResponse(e)
    elif request.method == 'GET':
        return render(request, 'jungle/upload.html')

