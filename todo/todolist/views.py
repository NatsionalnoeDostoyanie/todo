from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout

from .models import Task


@login_required(login_url='login')
def index(request):
    template_name = 'index.html'
    task_list = Task.objects.filter(user=request.user)
    context = {
        'task_list': task_list,
        'title': 'Главная страница',
    }
    return render(request, template_name, context)


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    task = Task.objects.create(title=title, user=request.user)
    return redirect('index')


@require_http_methods(["POST"])
def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('index')


@require_http_methods(["POST"])
def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль')

    return render(request, 'login.html')


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')
