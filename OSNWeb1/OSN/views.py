from django.shortcuts import render

from .models import Soal

# Create your views here.
def index(request):
    posts = Soal.objects.all()

    return render(request, 'OSN/index.html', {'posts': posts})

def detail(request, pk):
    post = Soal.objects.get(pk=pk)

    return render(request, 'OSN/detail.html', {'post': post})