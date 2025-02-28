from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    api_home,
    MoodSurveyViewSet,
    index,
    create_mood_survey,  # Убедитесь, что эта функция импортирована, если она используется
    home,
    mood_recommendation,
)

# Создаем экземпляр маршрутизатора
router = DefaultRouter()
router.register(r'mood-surveys', MoodSurveyViewSet, basename='moodsurveys')

# Определяем маршруты
urlpatterns = [
    path('api/home/', api_home, name='api-home'),  # Маршрут для API домашней страницы
    path('', index, name='index'),  # Этот маршрут будет привязан к корню приложения
    path('home/', home, name='home'),  # Маршрут для страницы home
    path('mood_recommendation/', mood_recommendation, name='mood_recommendation'),  # Маршрут для страницы рекомендаций
    path('api/recommendation/', mood_recommendation, name='get_recommendation'),  # Исправлено: используем правильную функцию
    path('api/mood-surveys/create/', create_mood_survey, name='create_mood_survey'),  # Добавлен маршрут для создания опроса настроения
] + router.urls  # Добавляем маршруты из маршрутизатора
