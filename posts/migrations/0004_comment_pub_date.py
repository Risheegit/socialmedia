# Generated by Django 4.0.6 on 2022-07-13 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]