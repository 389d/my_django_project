from rest_framework import serializers
from django.contrib.auth.models import User  # Импортируем модель User
from .models import MoodSurvey, NotificationSetting  # Импортируем ваши модели

# Определение сериализатора для модели User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Укажите необходимые поля

# Определение сериализатора для модели MoodSurvey
class MoodSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodSurvey
        fields = '__all__'  # Или укажите конкретные поля

# Определение сериализатора для модели NotificationSetting
class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = ['user', 'frequency', 'enabled']  # Укажите необходимые поля
