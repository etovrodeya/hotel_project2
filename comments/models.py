from django.db import models
from django.conf import settings

class Comment (models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
        )
    title=models.CharField(
        'Заголовок',
        max_length=140
        )
    comment = models.CharField(
        'Отзыв',
        max_length=500
        )
    date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'