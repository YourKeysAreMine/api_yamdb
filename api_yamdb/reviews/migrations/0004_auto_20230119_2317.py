# Generated by Django 3.2 on 2023-01-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230119_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='titles', through='reviews.Genre_Title', to='reviews.Genre'),
        ),
    ]
