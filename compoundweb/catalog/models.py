from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Compound(models.Model):
    name = models.CharField(max_length=30)
    smiles = models.CharField(max_length=50)
    inchlkey = models.CharField(max_length=50)
    c_set = models.CharField(max_length=30,default="N")
    # c_set = models.ManyToManyField(Library)
    def __str__(self):
        return f"{self.name} {self.smiles} {self.inchlkey} {self.c_set}"