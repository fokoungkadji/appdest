# Generated by Django 5.0.4 on 2024-04-04 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateures',
            name='description',
        ),
        migrations.RemoveField(
            model_name='utilisateures',
            name='surename',
        ),
        migrations.AddField(
            model_name='utilisateures',
            name='email',
            field=models.EmailField(default='kfb@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='utilisateures',
            name='message',
            field=models.TextField(default='message'),
        ),
    ]
