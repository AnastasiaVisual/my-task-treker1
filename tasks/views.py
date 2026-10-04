from django import tasks
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

@login_required
def task_list(request):   
    tasks = Task.objects.filter(owner=request.user)
    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

@login_required
def toggle_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.is_done = not task.is_done
    task.save()
    return redirect("task_list")

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return JsonResponse({
                "success": True,
                "id": task.pk,
                "title": task.title,
                "category": task.category,
                "deadline": task.deadline.strftime("%d.%m.%Y") if task.deadline else "",
            })
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {'form': form, "tasks": Task.objects.filter(owner=request.user)})
