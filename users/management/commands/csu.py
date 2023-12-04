from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='kipriyn.dima1997@gmail.com',
            first_name='Admin',
            last_name='MLD',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('65900')
        user.save()