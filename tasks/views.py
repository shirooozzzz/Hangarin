from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Task, Category, Priority, SubTask, Note


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



class CategoryList(ListView):
    model = Category
    template_name = "category_list.html"
    paginate_by = 10


class CategoryCreate(CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("category_list")


class CategoryUpdate(UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("category_list")


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")


class PriorityList(ListView):
    model = Priority
    template_name = "priority_list.html"
    paginate_by = 10


class PriorityCreate(CreateView):
    model = Priority
    fields = "__all__"
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority_list")


class PriorityUpdate(UpdateView):
    model = Priority
    fields = "__all__"
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority_list")


class PriorityDelete(DeleteView):
    model = Priority
    template_name = "priority_confirm_delete.html"
    success_url = reverse_lazy("priority_list")


class SubTaskList(ListView):
    model = SubTask
    template_name = "subtask_list.html"
    paginate_by = 10


class SubTaskCreate(CreateView):
    model = SubTask
    fields = "__all__"
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask_list")


class SubTaskUpdate(UpdateView):
    model = SubTask
    fields = "__all__"
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask_list")


class SubTaskDelete(DeleteView):
    model = SubTask
    template_name = "subtask_confirm_delete.html"
    success_url = reverse_lazy("subtask_list")


class NoteList(ListView):
    model = Note
    template_name = "note_list.html"
    paginate_by = 10


class NoteCreate(CreateView):
    model = Note
    fields = "__all__"
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")


class NoteUpdate(UpdateView):
    model = Note
    fields = "__all__"
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")


class NoteDelete(DeleteView):
    model = Note
    template_name = "note_confirm_delete.html"
    success_url = reverse_lazy("note_list")