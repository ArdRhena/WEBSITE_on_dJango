from django.shortcuts import render, redirect
from .models import TaskManager
from .form import TaskManagerForm

def index(request):
    tasks = TaskManager.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ""
    if request.method == "POST":
        form = TaskManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Error form"

    form = TaskManagerForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html', context)
