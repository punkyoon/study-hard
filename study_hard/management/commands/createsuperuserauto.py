from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    def handle(self, *args, **options):
        pw = get_random_string()
        with open('pw.txt', 'w') as pwfile:
            pwfile.write(pw)

        print('Generated root password: %s' % (pw,))

        admin = User.objects.create_superuser(
            email='root@localhost',
            username='root',
            password=pw,
        )

        admin.is_active = True
        admin.is_admin = True
        admin.save()
