from rest_framework import serializers
from absence.models import Etudiant,Cours,Absence

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Etudiant 
        fields=('id_etudiant','nom','prenom')

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Absence 
        fields=('id_etudiant','id_cours','nombre_heures_absence','date_absence')

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cours 
        fields=('id_cours','nom_cours')