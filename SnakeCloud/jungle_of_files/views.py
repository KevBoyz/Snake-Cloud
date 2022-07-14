from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/auth/login/')
def dashboard(request):
    posts = FilePost.objects.all
    return render(request, 'jungle/dashboard.html', {'posts': posts})


@login_required(login_url='/auth/login/')
def dashboard_post(request, id):
    post = FilePost.objects.get(id=id)
    return render(request, 'jungle/dashboard_post.html', {'post': post})


@login_required(login_url='/auth/login/')
def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('upload_file')
        image = request.FILES.get('card_image')
        try:
            file_upload = FilePost.objects.create(
                user=request.user,
                title=title,
                description=description,
                file=file,
            )
            file_upload.save()
            return redirect('dashboard')
        except Exception as e:
            return HttpResponse(e)
    elif request.method == 'GET':
        return render(request, 'jungle/upload.html')

