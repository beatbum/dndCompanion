from django.db import models

# Create your models here.

class combatant(models.Model):
    hp = models.IntegerField(default=0)
    initiative = models.IntegerField(default = 1)

