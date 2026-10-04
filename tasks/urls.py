from django.urls import path
from .import views

urlpatterns=[
    path("", views.task_list, name="task_list"),
    path("tasks/<int:pk>/toggle/", views.toggle_task_done, name="task-toggle"),
    path("tasks/new/", views.task_create, name="task_create"),
]