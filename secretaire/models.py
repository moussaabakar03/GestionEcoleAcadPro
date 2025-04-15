from django.db import models

# Create your models here.

from django.db import models

class Classe(models.Model):
    classe = models.CharField(max_length=100, unique=True)
    capacite = models.PositiveIntegerField(default=1)  
    scolarite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.classe} ({self.capacite} élèves)"
    
    
class SalleDeClasse(models.Model):
    niveau = models.ForeignKey(Classe, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50, unique=True)
    capacite = models.PositiveIntegerField()
    emplacement = models.CharField(max_length=100, null=True, blank=True)
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
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, blank=True)
    salleDeClasse_id = models.ForeignKey(SalleDeClasse, on_delete=models.CASCADE, null=True, blank=True)
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
    mail = models.EmailField()
    niveau = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    nationnalite = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/etudiants/', null=True, blank=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    # lieuDeNaissance = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.matricule}- {self.nom} {self.prenom}"


class Enseignant(models.Model):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    diplome = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/enseignants/', null=True, blank=True)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    mail = models.EmailField()
    lieuDeNaissance = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    typeDeContrat = models.CharField(max_length=100)
    date_debut_contrat = models.DateField()
    date_fin_contrat = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"

    
class Matiere(models.Model):
    code = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True)
    niveau = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    coefficient = models.PositiveIntegerField()

