# Generated by Django 5.1.1 on 2024-09-16 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_turn_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='startinghand',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.game'),
        ),
        migrations.AddField(
            model_name='turn',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.game'),
        ),
    ]
