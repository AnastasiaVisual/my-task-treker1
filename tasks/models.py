from django.db import models

class Task(models.Model):
   STATUS_CHOICES = [
        ('todo', 'Не выполнена'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнена'),
    ]
   PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
   
   title = models.CharField(max_length=200, verbose_name='Название')

   description = models.TextField(verbose_name='Описание')

   status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo', verbose_name='Статус')

   priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name='Приоритет')

   deadline = models.DateTimeField(null=True, blank=True, verbose_name='Дедлайн')

   category = models.CharField(max_length=100, blank=True, verbose_name='Категория')

   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

   updated_at = models.DateTimeField( auto_now=True, verbose_name='Дата изменения')

   def __str__(self):
        return self.title
