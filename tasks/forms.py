from django import forms
from .models import Task, Category, Priority, Note, SubTask

from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control"
                },
                format="%Y-%m-%dT%H:%M"
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.deadline:
            self.initial["deadline"] = self.instance.deadline.strftime("%Y-%m-%dT%H:%M")


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