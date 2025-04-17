from django.db import models

# Create your models here.

from django.db import models

class Classe(models.Model):
    classe = models.CharField(max_length=100, unique=True)
    # capacite = models.PositiveIntegerField(default=1)  
    # scolarite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.classe}"
    
    
class SalleDeClasse(models.Model):
    niveau = models.ForeignKey(Classe, on_delete=models.CASCADE, null =True, blank=True, related_name='salle_de_classe')
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
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, blank=True, related_name= 'etudiant')
    # salleDeClasse_id = models.ForeignKey(SalleDeClasse, on_delete=models.CASCADE, null=True, blank=True)
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
    lieuDeNaissance = models.CharField(max_length=100)

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


class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True,  related_name='inscriptions')
    salleClasse = models.ForeignKey(SalleDeClasse, on_delete=models.CASCADE, null=True, blank=True)
    dateEnregistrement = models.DateTimeField(auto_now_add=True)
    # coutA = models.DecimalField(max_digits=10, decimal_places=2)
    montantVerse = models.DecimalField(max_digits=10, decimal_places=2)
    # montantRestant = models.DecimalField(max_digits=10, decimal_places=2)
    
class Scolarite(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True)
    coutScolarite = models.DecimalField(max_digits=10, decimal_places=2)
    montantPaye = models.DecimalField(max_digits=10, decimal_places=2)
    montantRestant = models.DecimalField(max_digits=10, decimal_places=2)
    etat = models.CharField(max_length=100, choices=[('Reglé', 'Reglé'), ('A completé', 'A completé')])
    
    
class Cours(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=True, blank=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True)
    dateDebutCours = models.DateField()
    dureeCours = models.PositiveIntegerField()
    trimestre = models.CharField(max_length=100, choices=[('Trimestre 1', 'Trimestre 1'), ('Trimestre 2', 'Trimestre 2'), ('Trimestre 3', 'Trimestre 3' )])
    # typeDeCours = models.CharField(max_length=100, choices=[('Normal', 'Normal'), ('Rattrapage', 'Rattrapage') ])
    etat = models.CharField(max_length=100, choices=[('En cours', 'En cours'), ('Effectué', 'Effectué'), ('Planifié', 'Planifié')])


class Evaluation(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, null=False, blank=True)
    trimestre = models.CharField(max_length=100, choices=[('Trimestre 1', 'Trimestre 1'), ('Trimestre 2', 'Trimestre 2'), ('Trimestre 3', 'Trimestre 3')])
    typeEvaluation = models.CharField(max_length=100, choices=[('Devoir', 'Devoir'), ('Interrogation', 'Interrogation'), ('Composition', 'Composition')])
    dateEvaluation = models.DateField()
    note = models.DecimalField(max_digits=10, decimal_places=2)
    
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True, related_name='evaluations')
    

class Cout(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True, related_name='couts')
    coutInscription = models.DecimalField(max_digits=10, decimal_places=2)
    coutScolarite = models.DecimalField(max_digits=10, decimal_places=2)
    fraisEtudeDossier = models.DecimalField(max_digits=10, decimal_places=2)
    
    