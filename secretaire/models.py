from django.db import models

# Create your models here.

from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    date_naissance = models.DateField()
    groupe_sanguin = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'), 
        ('B+', 'B+'), ('B-', 'B-'), 
        ('AB+', 'AB+'), ('AB-', 'AB-'), 
        ('O+', 'O+'), ('O-', 'O-')
    ])
    mail = models.EmailField(unique=True)
    salleDeClasse = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    nationnalite = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/etudiants/', null=True, blank=True)

    def __str__(self):
        return f"{self.matricule}- {self.nom} {self.prenom}"


class Enseignant(models.Model):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    tel = models.CharField(max_length=15, unique=True)
    diplome = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/enseignants/', null=True, blank=True)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    mail = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.profession}"
    
    
class Classe(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} - {self.niveau}"

class SalleDeClasse(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    capacite = models.PositiveIntegerField()
    emplacement = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Salle {self.nom} (Capacité: {self.capacite})"