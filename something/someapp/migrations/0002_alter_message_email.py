# Generated by Django 4.2.3 on 2024-03-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('someapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
