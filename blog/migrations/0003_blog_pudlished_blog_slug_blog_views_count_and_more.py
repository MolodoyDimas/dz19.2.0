# Generated by Django 4.2.7 on 2023-11-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_creation_date_blog_image_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pudlished',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=100, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
