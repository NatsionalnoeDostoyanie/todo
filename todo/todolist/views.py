# If hints for 'objects' do not work, use 'pip install django-stubs'

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .forms import TaskForm

from .models import Task


@login_required(login_url='login')
def index(request):
    template_name = 'index.html'
    task_list = Task.objects.filter(user=request.user)
    form = TaskForm()
    context = {
        'task_list': task_list,
        'title': 'Главная страница',
        'form': form
    }
    return render(request, template_name, context)


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()

    return redirect('index')


def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)

    return redirect('index')


@require_http_methods(["POST"])
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('index')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': form})
