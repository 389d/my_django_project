from .base import *

DEBUG = False  # Выключите режим отладки для тестирования

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Настройки базы данных для тестирования
DATABASES['default']['NAME'] = os.getenv('DJANGO_DATABASE_NAME', 'test_db')
