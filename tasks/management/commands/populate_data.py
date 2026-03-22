from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.utils import timezone

from tasks.models import Task, Note, SubTask, Category, Priority


class Command(BaseCommand):
    help = "Generate fake tasks, notes, and subtasks"

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = Category.objects.all()
        priorities = Priority.objects.all()

        status_choices = ["Pending", "In Progress", "Completed"]

        for _ in range(20):

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_year()),
                status=fake.random_element(elements=status_choices),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )

            for _ in range(random.randint(1,3)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph()
                )

            for _ in range(random.randint(1,4)):
                SubTask.objects.create(
                    task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=status_choices)
                )

        self.stdout.write(self.style.SUCCESS("Fake data generated successfully!"))