from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Task


def dashboard(request):

    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(status="Pending").count()
    completed_tasks = Task.objects.filter(status="Completed").count()

    recent_tasks = Task.objects.order_by("-created_at")[:5]

    context = {
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "recent_tasks": recent_tasks,
    }

    return render(request, "dashboard.html", context)


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description", "deadline", "status", "priority", "category"]
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "deadline", "status", "priority", "category"]
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task_list")