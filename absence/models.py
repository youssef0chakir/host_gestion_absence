from django.db import models

class Etudiant(models.Model):
    id_etudiant = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)

class Cours(models.Model):
    id_cours = models.IntegerField(primary_key=True)
    nom_cours = models.CharField(max_length=50)
 
class Absence(models.Model):
    id_etudiant = models.IntegerField()
    id_cours = models.IntegerField()
    nombre_heures_absence = models.IntegerField()
    date_absence = models.DateField()
 