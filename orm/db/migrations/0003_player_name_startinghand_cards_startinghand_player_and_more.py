# Generated by Django 5.1.1 on 2024-09-16 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_game_player_startinghand_turn_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='startinghand',
            name='cards',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='startinghand',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.player'),
        ),
        migrations.AddField(
            model_name='startinghand',
            name='turn_order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='turn',
            name='card_used',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='turn',
            name='discard_choice',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='turn',
            name='draw_choice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='turn',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.player'),
        ),
        migrations.AddField(
            model_name='turn',
            name='turn_number',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='turn',
            name='turn_type',
            field=models.CharField(choices=[('NONE', 'None'), ('DISCARD', 'Discard'), ('DRAW', 'Draw')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='seed',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
