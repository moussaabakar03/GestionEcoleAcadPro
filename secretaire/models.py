from django.db import models

# Create your models here.

from django.db import models


class SalleDeClasse(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    capacite = models.PositiveIntegerField()
    emplacement = models.CharField(max_length=100, null=True, blank=True)
    niveau = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return f"{self.niveau}- {self.nom}- {self.capacite}"
    
class Parent(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    lien_de_parente = models.CharField(
        max_length=50,
        choices=[
            ('Père', 'Père'),
            ('Mère', 'Mère'),
            ('Tuteur', 'Tuteur'),
        ]
    )
    photo = models.ImageField(upload_to='parents/', null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, blank=True)
    matricule = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    date_naissance = models.DateField()
    groupe_sanguin = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'), 
        ('B+', 'B+'), ('B-', 'B-'), 
        ('AB+', 'AB+'), ('AB-', 'AB-'), 
        ('O+', 'O+'), ('O-', 'O-')
    ])
    mail = models.EmailField()
    salleDeClasse_id = models.ForeignKey(SalleDeClasse, on_delete=models.CASCADE, null=True, blank=True)
    niveau = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    nationnalite = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/etudiants/', null=True, blank=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    

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
        return f"{self.nom} {self.prenom}"
    
    
class Classe(models.Model):
    nom = models.CharField(max_length=100, unique=True)         # à supp
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} - {self.niveau}"

    
class Matiere(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    niveau = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True)
    coefficient = models.PositiveIntegerField()

