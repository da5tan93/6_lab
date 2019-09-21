# Generated by Django 2.2.5 on 2019-09-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190921_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=200, null=True, verbose_name='Статус'),
        ),
    ]