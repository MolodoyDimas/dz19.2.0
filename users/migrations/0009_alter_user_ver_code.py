# Generated by Django 4.2.7 on 2023-12-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='169216789495', max_length=15, verbose_name='Проверочный код'),
        ),
    ]