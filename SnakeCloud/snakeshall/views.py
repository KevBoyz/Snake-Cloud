from django.shortcuts import render
from .forms import QuillFieldForm
from .models import QuillPost


def test(request):
    if request.method == 'POST':
        if not request.POST.get('content'):
            return render(request, 'hall/test.html', {'form': QuillFieldForm()})
        else:
            quill = QuillPost(
                content=request.POST.get('content')
            )
            quill.save()
    return render(request, 'hall/test.html', {'form': QuillFieldForm()})
