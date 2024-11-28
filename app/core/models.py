from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)  # Название видео
    video_file = models.FileField(upload_to='videos/')  # Файл видео
    access_date = models.DateField()  # Дата, с которой видео становится доступным
    week_number = models.PositiveIntegerField(unique=True)  # Номер недели

    def __str__(self):
        return f"Week {self.week_number}: {self.title}"