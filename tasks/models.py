import django
from django.db import models
from django.conf import settings

class Task(models.Model):
   owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
   title = models.CharField(max_length=200, verbose_name='Название')
   description = models.TextField(verbose_name='Описание')
   is_done = models.BooleanField(default=False)
   deadline = models.DateField(null=True, blank=True, verbose_name='Дедлайн')
   category = models.CharField(max_length=100, blank=True, verbose_name='Категория')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
   updated_at = models. DateTimeField( auto_now=True, verbose_name='Дата изменения')

   def __str__(self):
        return self.title
