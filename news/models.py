from django.db import models
from django.utils import timezone

# Create your models here.

#минимальные элементы: текст, заголовок, дата отправления, автор, список тегов, количество просмотров

class Post(models.Model): #возможно лучше изменить на Post, а все новости в целом оставить News
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    counter = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title