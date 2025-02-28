from django.db import models
from django.contrib.auth.models import User

class NotificationSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    frequency = models.IntegerField(help_text='Frequency in minutes')
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Notification Settings"

class MoodSurvey(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)  # День недели
    mood = models.CharField(max_length=50)  # Настроение
    comment = models.TextField(blank=True, null=True)  # Комментарий пользователя
    date_created = models.DateTimeField(auto_now_add=True)  # Дата создания записи

    def __str__(self):
        return f"{self.user.username} - {self.day}: {self.mood}"
