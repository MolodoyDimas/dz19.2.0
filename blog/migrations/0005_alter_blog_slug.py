# Generated by Django 4.2.7 on 2023-12-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
    ]
