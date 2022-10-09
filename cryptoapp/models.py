from django.db import models

class Tutorial(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nazwa")
    content = models.TextField(verbose_name="Treść")

    def __str__(self):
        return self.name

class Blockchain(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nazwa")
    description = models.TextField(verbose_name="Opis")

    def __str__(self):
        return self.name

class Dict(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nazwa")
    description = models.TextField(verbose_name="Opis")

    def __str__(self):
        return self.name

class Basic(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nazwa")
    description = models.TextField(verbose_name="Opis")

    def __str__(self):
        return self.name

class Token(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nazwa")
    shortcut = models.CharField(max_length=6,verbose_name="Ticker")
    blockchain =  models.ForeignKey(
        Blockchain, on_delete=models.SET_NULL, verbose_name="Sieć",
        null=True, default=None, blank=True)
    description = models.TextField(verbose_name="Opis")

    def __str__(self):
        return self.shortcut