# Generated by Django 4.2.7 on 2023-12-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='808990544675', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
