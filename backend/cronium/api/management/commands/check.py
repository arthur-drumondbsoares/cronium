from django.core.management.base import BaseCommand
from ...models import User, Task

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.get(id=1)
        tasks = Task.objects.filter(user=user)
        self.stdout.write(self.style.SUCCESS(tasks))