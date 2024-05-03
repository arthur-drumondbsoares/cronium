from django.core.management.base import BaseCommand
from ...models import User
from faker import Faker

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        faker = Faker()
        for i in range(2):
            instance = User.objects.create(
                username = faker.name(),
                email = faker.email(),
                password = faker.password()
            )
            instance.save()
        self.stdout.write(self.style.SUCCESS('Fake data populated successfully'))



            
