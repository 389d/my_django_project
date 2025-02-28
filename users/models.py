from django.db import models
class NotificationSetting(models.Model):
    name = models.CharField(max_length=100)
    value = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Create your models here.
