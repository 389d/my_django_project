from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MoodSurvey, NotificationSetting  # Импортируйте ваши модели
from .serializers import UserSerializer, MoodSurveySerializer, NotificationSettingSerializer  # Импортируйте ваши сериализаторы
from django_filters.rest_framework import DjangoFilterBackend  # Правильный импорт
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

# Функция для отображения домашней страницы
def home(request):
    return render(request, 'home.html')  # Убедитесь, что имя файла указано правильно

# Функция для отображения страницы index
def index(request):
    return render(request, 'index.html')  # Замените 'index.html' на ваш шаблон

# Представление для регистрации
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet для MoodSurvey
class MoodSurveyViewSet(viewsets.ModelViewSet):
    queryset = MoodSurvey.objects.all()
    serializer_class = MoodSurveySerializer
    filter_backends = (DjangoFilterBackend,)  # Используем правильный импорт
    filterset_fields = ['user', 'mood', 'date']

# ViewSet для NotificationSetting
class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['user', 'setting_type']

# API для получения всех настроек уведомлений
@api_view(['GET'])
def notification_settings(request):
    logger.info("Received request for notification settings")
    settings = NotificationSetting.objects.all()
    serializer = NotificationSettingSerializer(settings, many=True)
    return Response(serializer.data)

# API для получения всех опросов настроения
@api_view(['GET'])
def mood_surveys(request):
    logger.info("Received request for mood surveys")
    surveys = MoodSurvey.objects.all()
    serializer = MoodSurveySerializer(surveys, many=True)
    return Response(serializer.data)

# API для создания нового опроса настроения
@api_view(['POST'])
def create_mood_survey(request):
    logger.info("Received request to create a mood survey")
    serializer = MoodSurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info("Mood survey created successfully")
        return Response(serializer.data, status=201)
    logger.error(f"Failed to create mood survey: {serializer.errors}")
    return Response(serializer.errors, status=400)

# API для получения рекомендаций по настроению
@api_view(['GET'])
def mood_recommendation(request):
    mood = request.GET.get('mood', None)
    logger.info(f"Received request for mood recommendation with mood: {mood}")
    recommendations = {
        'Счастлив': "Отлично! Продолжай делать то, что радует!",
        'Грустный': "Попробуй провести время с друзьями или заняться спортом.",
        'Нейтральный': "Как насчет того, чтобы попробовать что-то новое?",
    }
    recommendation_text = recommendations.get(mood, "Не знаю, как помочь!")
    return Response({'recommendation': recommendation_text})

# Добавление функции api_home
@api_view(['GET'])
def api_home(request):
    logger.info("Received request at api_home")
    return Response({"message": "Welcome to the API!"})
