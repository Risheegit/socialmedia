# Generated by Django 4.0.6 on 2022-07-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reportcount',
            field=models.IntegerField(default=0),
        ),
    ]