from django.db import models

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    ecole = models.CharField(max_length=100)
    langue = models.CharField(max_length=100)
    # Ajoutez d'autres champs pour les informations des étudiants

class Question(models.Model):
    diplome = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100)
    # Ajoutez d'autres champs pour les informations des questions

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)