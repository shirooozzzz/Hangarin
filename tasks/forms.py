from django import forms
from .models import Task, Category, Priority, Note, SubTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"