# Generated by Django 5.1.3 on 2024-11-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_startinghand_game_turn_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='turn',
            name='computational_time',
            field=models.FloatField(default=0.0),
        ),
    ]
