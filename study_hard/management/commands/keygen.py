import json

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    def handle(self, *args, **options):
        chars = 'qwertyuiopasdfghjklzxcvbnm0987654321!@#$%^&*(-_=+)'
        SECRET_KEY = get_random_string(50, chars)

        data = {
            'SECRET_KEY': SECRET_KEY,
        }

        with open('secret.key', 'w') as f:
            json.dump(data, f)

        print('[SUCCESS] secret.key is generated!')
