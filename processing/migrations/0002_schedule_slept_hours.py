# Generated by Django 3.1.2 on 2020-12-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='Slept_hours',
            field=models.IntegerField(default=6),
        ),
    ]