from django.db import models

# Create your models here.

class Ricetta(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=30)
    ingredienti = models.CharField(max_length=2000)
    difficoltà = models.IntegerField(default=1)
    tempo = models.IntegerField(default=1)
    descrizione = models.CharField(max_length=50000)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Utente(models.Model):
    nickname = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    password = models.CharField(max_length=8)
    preferiti = models.ManyToManyField(Ricetta, blank=True)

    def __str__(self):
        return self.nickname