# Generated by Django 4.2.7 on 2023-11-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.CharField(default=0, max_length=100, verbose_name='Создан'),
            preserve_default=False,
        ),
    ]
