# Generated by Django 4.0.3 on 2022-04-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='place_of_birth',
            field=models.CharField(max_length=255),
        ),
    ]