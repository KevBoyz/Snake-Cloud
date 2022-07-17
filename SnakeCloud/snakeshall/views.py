from django.shortcuts import render
from .forms import QuillFieldForm
from .models import QuillPost
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def dashboard(request):
    articles = QuillPost.objects.all()
    return render(request, 'hall/dashboard.html', {'articles': articles})


@login_required(login_url='/auth/login/')
def new_article(request):
    if request.method == 'POST':
        if not request.POST.get('content'):
            return render(request, 'hall/test.html', {'form': QuillFieldForm()})
        else:
            quill = QuillPost(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                admin=request.user,
                content=request.POST.get('content')
            )
            quill.save()
    return render(request, 'hall/new_article.html', {'form': QuillFieldForm()})


@login_required(login_url='/auth/login/')
def article(request, article):
    if request.method == 'GET':
        article = QuillPost.objects.get(title=article)
        return render(request, 'hall/article.html', {'article': article})


