# Generated by Django 4.2.7 on 2023-12-02 11:39

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_id_alter_weather_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=60, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
