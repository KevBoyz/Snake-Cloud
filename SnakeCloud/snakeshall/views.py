from django.shortcuts import render
from .forms import QuillFieldForm
import ast


def test(request):
    if request.method == 'POST':
        if not request.POST.get('content'):
            return render(request, 'hall/test.html', {'form': QuillFieldForm()})
        else:
            html = ast.literal_eval(request.POST.get('content'))['html']
    return render(request, 'hall/test.html', {'form': QuillFieldForm()})
