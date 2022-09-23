from statistics import mode
from django.db import models

class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name