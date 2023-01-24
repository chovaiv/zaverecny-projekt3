from django.db import models
from colorfield.fields import ColorField

class Graf(models.Model):
    jmeno_objektu = models.CharField(max_length=200)
    pocet_objektu = models.IntegerField()
    color = ColorField(default='#000000')
    borderColor = ColorField(default='#FF00FF', format="hexa")

    def __str__(self):
        return "{} - {}".format(self.jmeno_objektu, self.pocet_objektu)

class Bar(models.Model):
    jmeno = models.CharField(max_length=299)
    pocet = models.IntegerField()
    color = ColorField(default='#0010EE')
    borderColor = ColorField(default= '#0010EE')
    label = models.CharField(max_length=30, default="Label")

    def __str__(self):
        return "{} - {}".format(self.jmeno, self.pocet)

class Typ(models.Model):
    jmeno_grafu = models.CharField(max_length=20)
    obrazek = models.ImageField(upload_to='images/')

    def __str__(self):
        return "{}".format(self.jmeno_grafu)