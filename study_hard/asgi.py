# ASGI config for study_hard project
import os
from channels.asgi import get_channel_layer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_hard.settings')
channel_layer = get_channel_layer()
