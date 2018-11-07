from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Monster(models.Model):
    name = models.CharField(max_length = 20)
    hp = models.IntegerField(default = 0)
    # Stat block
    str = models.IntegerField(default = 0)
    dex = models.IntegerField(default = 0)
    char = models.IntegerField(default = 0)
    wis = models.IntegerField(default = 0)
    int = models.IntegerField(default = 0)
    char = models.IntegerField(default = 0)
    # Special Abilities
    special_abilities = ArrayField(models.CharField(max_length = 200))
