from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Category, Priority, SubTask, Note
from .forms import TaskForm


def dashboard(request):

    total_tasks = Task.objects.count()
    pending_tasks = Task.objects.filter(status="Pending").count()
    completed_tasks = Task.objects.filter(status="Completed").count()
    overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(), status__in=["Pending", "In Progress"])


    recent_tasks = Task.objects.order_by("-created_at")[:5]

    context = {
        "total_tasks": Task.objects.count(),
        "pending_tasks": Task.objects.filter(status="Pending").count(),
        "completed_tasks": Task.objects.filter(status="Completed").count(),
        "recent_tasks": Task.objects.order_by('-id')[:10],
        "now": timezone.now(),
    }

    return render(request, "dashboard.html", context)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        search_query = self.request.GET.get("q")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(status__icontains=search_query)
            )

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("task_list")



class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Category.objects.all()
        search_query = self.request.GET.get("q")

        if search_query and search_query.strip():
            queryset = queryset.filter(
                name__icontains=search_query
            )

        return queryset


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("category_list")


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("category_list")


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")


class PriorityList(LoginRequiredMixin, ListView):
    model = Priority
    template_name = "priority_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Priority.objects.all()
        search_query = self.request.GET.get("q")

        if search_query and search_query.strip():
            queryset = queryset.filter(
                name__icontains=search_query
            )

        return queryset


class PriorityCreate(LoginRequiredMixin, CreateView):
    model = Priority
    fields = "__all__"
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority_list")


class PriorityUpdate(LoginRequiredMixin, UpdateView):
    model = Priority
    fields = "__all__"
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority_list")


class PriorityDelete(LoginRequiredMixin, DeleteView):
    model = Priority
    template_name = "priority_confirm_delete.html"
    success_url = reverse_lazy("priority_list")


class SubTaskList(LoginRequiredMixin, ListView):
    model = SubTask
    template_name = "subtask_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = SubTask.objects.all()
        search_query = self.request.GET.get("q")

        if search_query and search_query.strip():
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(task__title__icontains=search_query)
            )

        return queryset


class SubTaskCreate(LoginRequiredMixin, CreateView):
    model = SubTask
    fields = "__all__"
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask_list")


class SubTaskUpdate(LoginRequiredMixin, UpdateView):
    model = SubTask
    fields = "__all__"
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask_list")


class SubTaskDelete(LoginRequiredMixin, DeleteView):
    model = SubTask
    template_name = "subtask_confirm_delete.html"
    success_url = reverse_lazy("subtask_list")


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = "note_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Note.objects.all()
        search_query = self.request.GET.get("q")

        if search_query and search_query.strip():
            queryset = queryset.filter(
                Q(content__icontains=search_query) |
                Q(task__title__icontains=search_query)
            )

        return queryset


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = "__all__"
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = "__all__"
    template_name = "note_form.html"
    success_url = reverse_lazy("note_list")


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "note_confirm_delete.html"
    success_url = reverse_lazy("note_list")