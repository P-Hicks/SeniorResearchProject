# db/models.py
from django.db import models

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# define models here
class Game(Model):
    seed = models.CharField(null=True, max_length=255)
    
class Player(Model):
    name = models.CharField(null=True, max_length=255)
    

class StartingHand(Model):
    turn_order = models.IntegerField(null=False,blank=False, default=1)
    cards = models.CharField(null=True, max_length=255)
    player = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        null=True,
    )

class Turn(Model):
    class Types(models.TextChoices):
        NONE = "NONE", "None"
        DISCARD = "DISCARD", "Discard"
        DRAW = "DRAW", "Draw" 

    turn_type = models.CharField(
        max_length=10,
        choices=Types.choices,
        null=True
    )
    turn_number = models.IntegerField(null=False,blank=False,default=-1)
    draw_choice = models.IntegerField(null=True,)
    discard_choice = models.IntegerField(null=False,blank=False,default=-1)
    card_used = models.IntegerField(null=False,blank=False,default=-1)
    
    player = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        null=True
    )
