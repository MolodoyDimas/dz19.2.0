# Generated by Django 4.2.7 on 2023-12-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(verbose_name='Номер версии'),
        ),
    ]