# my_django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import home, api_home  # Импортируем представления home и api_home

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админ-панели
    path('', home, name='home'),  # Корневой маршрут, который использует ваше представление home
    path('api/home/', api_home, name='api_home'),  # Добавляем маршрут для api_home
    path('api/', include('myapp.urls')),  # Подключение маршрутов из приложения myapp
]
