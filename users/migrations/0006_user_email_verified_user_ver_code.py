# Generated by Django 4.2.7 on 2023-12-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_email_verification_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Верификация почты'),
        ),
        migrations.AddField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='031461288876', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
