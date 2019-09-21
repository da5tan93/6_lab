from django.db import models


class Visitor(models.Model):
    status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]
    author = models.CharField(default='Unknown', max_length=40, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(choices=status_choices, max_length=200, null=True, blank=True, default='active',
                              verbose_name='Статус')

    def __str__(self):
        return self.author

