# Generated by Django 4.0.4 on 2022-05-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]
