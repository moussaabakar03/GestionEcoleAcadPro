from django.contrib import messages

from django.shortcuts import get_object_or_404, render, redirect

from . models import Classe, Cours, Cout, Emargement, Etudiant, Enseignant, Evaluation, Inscription, Matiere, Parent, SalleDeClasse


from django.contrib.auth.forms import UserCreationForm 
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def index5(request):
    return render(request, 'index5.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login.html')


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('login')






#Etudiant
def all_student(request):
    inscription = Inscription.objects.all()
    if request.method == 'POST':
        matricule = request.POST['matricule']
        nom = request.POST.get('nom')        
        
        etudiant = Etudiant.objects.filter(matricule__icontains=matricule, nom__icontains=nom)
        
        context = {'etudiants': etudiant, 'inscription': inscription}
        return render(request, 'all-student.html', context)
    else:
        etudiant = Etudiant.objects.all()
        context = {'etudiants': etudiant, 'inscription': inscription}
        return render(request, 'all-student.html', context)


def admit_form(request):
    salles = SalleDeClasse.objects.all()
    parentss = Parent.objects.all()
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        matricule = request.POST["matricule"]
        genre = request.POST["genre"]
        date_naissance = request.POST["date_naissance"]
        groupe_sanguin = request.POST["groupe_sanguin"]
        mail = request.POST["mail"]
        # salleDeClasse_id = request.POST["salleDeClasse"]
        # niveau = request.POST["niveau"]
        telephone = request.POST["telephone"]
        nationnalite = request.POST["nationnalite"]
        photo = request.FILES.get("photo")
        parent = request.POST.get("parent")

        # salleDeClasse_id = request.POST.get("salleDeClasse")
       
        # salle = SalleDeClasse.objects.get(pk=int(salleDeClasse_id))
        parent_id = Parent.objects.get(pk=int(parent))

        
        # Vérifier si un étudiant avec le même matricule  déjà
        # if Etudiant.objects.filter(matricule=matricule).exists():
        #     return render(request, "admit-form.html", {"error": "Matricule déjà utilisé !"})

        # Enregistrement dans la base de données
        Etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            parent=parent_id,
            matricule=matricule,
            genre=genre,
            date_naissance=date_naissance,
            groupe_sanguin=groupe_sanguin,
            mail=mail,
            # salleDeClasse_id=salle,
            telephone=telephone,
            nationnalite=nationnalite,
            photo=photo
        )

        return redirect("all-student") 

    return render(request, "admit-form.html", {"salles": salles, "parentss": parentss})

def modifier_student(request, matricule):
    
    mtrcle = mtrcle = get_object_or_404(Etudiant, matricule=matricule)
    
    groupes_sanguins = ["A+", "A-", "B+", "B-", "O+", "O-"]
    sections = SalleDeClasse.objects.all()

    if request.method == "POST":
        mtrcle.nom = request.POST["nom"]
        mtrcle.prenom = request.POST["prenom"]
        parent_id = request.POST["parent"]
        mtrcle.matricule = request.POST["matricule"]
        mtrcle.genre = request.POST["genre"]
        mtrcle.date_naissance = request.POST["date_naissance"]
        mtrcle.groupe_sanguin = request.POST["groupe_sanguin"]
        mtrcle.mail = request.POST["mail"]
        # mtrcle.niveau = request.POST["niveau"]
        mtrcle.telephone = request.POST["telephone"]
        mtrcle.nationnalite = request.POST["nationnalite"]
        mtrcle.photo = request.FILES.get("photo")
        # mtrcle.salleDeClasse = SalleDeClasse.objects.get(pk=int(request.POST["salleDeClasse"]))

        mtrcle.parent = Parent.objects.get(pk=int(parent_id))
        
        mtrcle.save()
        return redirect("all-student")
    

    return render(request, "modifier-student.html", {
        "student": mtrcle,
        "groupes_sanguins": groupes_sanguins,
        "sections": sections,
        "parents": Parent.objects.all(),
    })

def supprimer_student(request, matricule):
    mtrcle = Etudiant.objects.get(matricule = matricule)
    if request.method == "GET":
        mtrcle.delete()
        return redirect("all-student")
    
def student_promotion(request):
    return render(request, 'student-promotion.html')

def student_detail(request, matricule):
    etudiant = Etudiant.objects.get(matricule = matricule)
    inscrits = etudiant.inscriptions.all()
    context = {"etudiant": etudiant, "inscrits": inscrits}
    return render(request, 'student-details.html', context)

def detailEtudiant(request, matricule, id):
    etudiant = Etudiant.objects.get(matricule = matricule)
    parent = Parent.objects.get(id = id)
    inscriptions = etudiant.inscriptions.all()
    evaluation = etudiant.evaluations.all()
    context = {"etudiant": etudiant, "parent": parent, "inscriptions": inscriptions, "evaluations": evaluation }
    return render(request, 'detailEtudiant.html', context)



#teacher
def all_teacher(request):
    enseignants = Enseignant.objects.all()
    content = {"enseignants": enseignants }
    return render(request, 'all-teacher.html', content)

def add_teacher(request):
    if request.method == "POST":
        matricule = request.POST["matricule"]
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        sexe = request.POST["sexe"]
        date_naissance = request.POST["date_naissance"]
        diplome = request.POST["diplome"]
        profession = request.POST["profession"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        photo = request.FILES.get("photo")  
        
        lieuDeNaissance = request.POST["lieuDeNaissance"]
        salaire = request.POST["salaire"]
        typeDeContrat = request.POST["typeDeContrat"]
        date_debut_contrat = request.POST["date_debut_contrat"]
        date_fin_contrat = request.POST["date_fin_contrat"]

    
        Enseignant.objects.create( matricule = matricule, nom = nom, prenom = prenom, profession = profession, tel = phone, 
                                diplome = diplome,  photo = photo , date_naissance = date_naissance, sexe = sexe, mail = email,
                                lieuDeNaissance= lieuDeNaissance, salaire = salaire, typeDeContrat = typeDeContrat, 
                                date_debut_contrat = date_debut_contrat, date_fin_contrat = date_fin_contrat)
        return redirect("all-teacher")
    return render(request, 'add-teacher.html')

def teacher_detail(request):
    return render(request, 'teacher-details.html')

def modifier_teacher(request, matricule):
    enseignant = Enseignant.objects.get(matricule = matricule)
    groupes_sanguins = ["A+", "A-", "B+", "B-", " AB+", "AB-", "O+", "O-"]
    if request.method == "POST":
        enseignant.matricule = request.POST["matricule"]
        enseignant.nom = request.POST["nom"]
        enseignant.prenom = request.POST["prenom"]
        enseignant.profession = request.POST["profession"]
        enseignant.tel = request.POST["phone"]
        enseignant.diplome = request.POST["diplome"]
        enseignant.photo = request.FILES.get("photo")
        enseignant.date_naissance = request.POST["date_naissance"]
        enseignant.sexe = request.POST["sexe"]
        enseignant.typeDeContrat = request.POST["typeContrat"]
        enseignant.mail = request.POST["email"]
        enseignant.save()
        return redirect("all-teacher")
    return render(request, 'modifier-teacher.html', {"enseignant": enseignant, "groupes_sanguins": groupes_sanguins})

def supprimer_teacher(request, matricule):
    enseignant = Enseignant.objects.get(matricule = matricule)
    enseignant.delete()
    return redirect("all-teacher")

def detailEnseignant(request, matricule):
    enseignant = Enseignant.objects.get(matricule = matricule)
    context = {"enseignant": enseignant}
    return render(request, 'detaitEnseignant.html', context)


#parent
def all_parents(request):
    parents = Parent.objects.all()
    return render(request, 'all-parents.html', {"parents": parents})

def add_parents(request):
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        genre = request.POST["genre"]
        telephone = request.POST["telephone"]
        email = request.POST["email"]
        profession = request.POST.get("profession", "")
        lien_de_parente = request.POST["lien_de_parente"]
        photo = request.FILES.get("photo")
        
        # Création de l'objet Parent
        Parent.objects.create(
            nom=nom,
            prenom=prenom,
            genre=genre,
            telephone=telephone,
            email=email,
            profession=profession,
            lien_de_parente=lien_de_parente,
            photo=photo
        )

        return redirect("all-parents")  # Redirige vers la liste des parents (à adapter selon ton URLconf)
    return render(request, 'add-parents.html')

def modifier_parent(request, id):
    parent = Parent.objects.get(id = id)
    if request.method == "POST":
        parent.nom = request.POST["nom"]
        parent.prenom = request.POST["prenom"]
        parent.genre = request.POST["genre"]
        parent.telephone = request.POST["telephone"]
        parent.email = request.POST["email"]
        parent.profession = request.POST.get("profession", "")
        parent.lien_de_parente = request.POST["lien_de_parente"]

        if "photo" in request.FILES:
            parent.photo = request.FILES["photo"]
        
        parent.save()
    
        return redirect("all-parents")
    
    return render(request, 'modifierParent.html', {"parent": parent})

def supprimer_parent(request, id):
    Parent.objects.get(id =id).delete()
    return redirect("all-parents")  # Redirige vers la liste des parents


#Matiere
def all_class(request):
    if request.method == "POST":
        nom = request.POST["nom"]
        # niveau = request.POST["niveau"]
        # classe = Classe.objects.get(classe = niveau)
        
        matiere = Matiere.objects.filter(
                nom__icontains=nom
            )

        return render(request, 'all-class.html', {"matieres": matiere})
    else:
        matiere = Matiere.objects.all()
        return render(request, 'all-class.html', {"matieres": matiere})

def add_class(request):
    enseignants = Enseignant.objects.all()
    niveaux = Classe.objects.all()
    content = {"enseignants": enseignants, "niveaux": niveaux}
    if request.method == "POST":
        nom = request.POST["nom"]
        niveau = request.POST["niveau"]
        coefficient = request.POST["coefficient"]
        description = request.POST.get("description", "")  # facultatif
        enseignant_id = request.POST["enseignant"]
        enseignant = Enseignant.objects.get(pk=int(enseignant_id))
        classe = Classe.objects.get(pk=int(niveau))
        
        if Matiere.objects.filter(nom=nom, niveau=classe).exists():
            messages.error(request, "Cette matière existe déjà")
        else:
            Matiere.objects.create(
                nom=nom,
                niveau=classe,
                coefficient=coefficient,
                description=description,
                enseignant=enseignant
            )
            # messages.success(request, "Matière ajoutée avec succès")
            return redirect("all-class")

    return render(request, 'add-class.html', content)

def supprimer_matiere(request, id):
    Matiere.objects.get(id=id).delete()
    return redirect("all-class")

def modifier_matiere(request, id):
    matiere = Matiere.objects.get(id=id)

    if request.method == "POST":
        matiere.nom = request.POST["nom"]
        # matiere.niveau = request.POST["niveau"]
        matiere.coefficient = request.POST["coefficient"]
        matiere.description = request.POST.get("description", "") 

        enseignant_id = request.POST["enseignant"]
        matiere.enseignant = Enseignant.objects.get(pk=int(enseignant_id))

        niveau_id = request.POST["niveau"]
        matiere.niveau = Classe.objects.get(pk=int(niveau_id))

        matiere.save()
        return redirect("all-class")
    return render(request, "modifierMatiere.html", {
        "matiere": matiere,
        "enseignants": Enseignant.objects.all(),
        "niveaux": Classe.objects.all()
    })



#salle de classe
def all_salle(request):
    salles = SalleDeClasse.objects.all()
    etudiant = Etudiant.objects.all()
    return render(request, 'all-salle.html', {"salles": salles, "etudiants": etudiant})

def add_salle(request):
    niveau = Classe.objects.all()
    if request.method == "POST":
        nom = request.POST["nom"]
        capacite = int(request.POST["capacite"])
        niveau = request.POST["niveau"]
        emplacement = request.POST.get("emplacement", "")  

        classe = Classe.objects.get(pk=int(niveau))
        
        # if SalleDeClasse.objects.get(nom =nom, niveau=classe).exists():
        #     messages.error(request, 'Cette salle existe deja')
        #     return redirect("all-salle")
        
        
        SalleDeClasse.objects.create(
            nom=nom,
            capacite=capacite,
            emplacement=emplacement,
            niveau = classe
        )

        return redirect("all-salle") 

    return render(request, 'add-salle.html', {"niveaux": niveau})

def modifierSalle(request, nom):
    salle = SalleDeClasse.objects.get(nom=nom)

    if request.method == "POST":
        salle.nom = request.POST["nom"]
        salle.capacite = int(request.POST["capacite"])
        salle.niveau = request.POST["niveau"]
        salle.emplacement = request.POST.get("emplacement", "")  # champ facultatif

        salle.save()
        return redirect('all-salle')

    return render(request, 'modifier_Salle.html', {"salle": salle})

def supprimerSalle(request, nom):
    SalleDeClasse.objects.get(nom=nom).delete()
    return redirect('all-salle')

def studentParSalle(request, id):
    salle = SalleDeClasse.objects.get(pk=id)
    if request.method == 'POST':
        matricule = request.POST['matricule']
        nom = request.POST.get('nom')        
        
        inscrit = Inscription.objects.filter(salleClasse=salle)
        
        inscrits = inscrit.filter(etudiant__matricule__icontains=matricule, etudiant__nom__icontains=nom)
        nombre = inscrits.count()
        return render(request, 'studentParSalle.html', {"salle": salle, 'inscrits': inscrits, 'nombre': nombre})
    else:
        inscrits = Inscription.objects.filter(salleClasse=salle)
        nombre = inscrits.count()
        return render(request, 'studentParSalle.html', {"salle": salle, 'inscrits': inscrits, 'nombre': nombre})

def listePresence(request, id):
    salle = SalleDeClasse.objects.get(pk=id)
    emargement = Emargement.objects.filter(salleClasse=salle)
    
    if request.method == 'POST':
        for em in emargement:
            # emargement = Emargement.objects.get(pk=em.pk)
            presence = request.POST.get(f"presence_{em.etudiant.matricule}")
            etudiant = Etudiant.objects.get(matricule=em.etudiant.matricule)
            
        dateHeureDebut = request.POST["dateHeureDebut"]
        commentaire = request.POST["commentaire"]
        
        Emargement.objects.create(
            salleClasse=salle,
            etudiant  =etudiant,
            dateHeureDebut = dateHeureDebut,
            commentaire = commentaire,
            presence = presence
        )    
        

        matricule = request.POST['matricule']
        nom = request.POST.get('nom')
        inscrit = Inscription.objects.filter(salleClasse=salle)
        inscrits = inscrit.filter(etudiant__matricule__icontains=matricule, etudiant__nom__icontains=nom)
        nombre = inscrits.count()
        
        return render(request, 'listePresence.html', {"salle": salle, 'inscrits': inscrits, 'nombre': nombre})
    else:
        inscrits = Inscription.objects.filter(salleClasse=salle)
        nombre = inscrits.count()
        return render(request, 'listePresence.html', {"salle": salle, 'inscrits': inscrits, 'nombre': nombre})




#Classe(niveau)
def all_niveau(request):
    niveaux = Classe.objects.all()
    return render(request, 'all-niveau.html', {"niveaux": niveaux})

def add_niveau(request):
    if request.method == "POST":
        classe = request.POST["classe"]
        # capacite = int(request.POST["capacite"])
        # scolarite = request.POST["scolarite"]
        
        Classe.objects.create(
            classe = classe,
            # capacite = capacite,
            # scolarite = scolarite
        )
        return redirect("all_niveau")
    return render(request, 'add-niveau.html')

def modifierNiveau(request, id):
    classe = Classe.objects.get(pk=id)
    if request.method == "POST":
        classe.classe = request.POST["classe"]
        classe.save()
        return redirect('all_niveau')
    return render(request, 'modifier-niveau.html', {"classe": classe})

def supprimerNiveau(request, id):
    Classe.objects.get(pk=id).delete()
    return redirect('all_niveau')

#Scolarité  add-scolarite.html
 
# def all_scolarite(request):
#     if request.method == 'POST':
#         classe = request.POST['classe']
#         coutScolarite = request.POST['coutScolarite']
#         montantPaye = request.POST['montantPaye']
#         montantRestant = request.POST['montantRestant']
#         etat = request.POST['etat']

        

#inscription  
# <td>{{ inscription.salleClasse.niveau.classe.couts }} F CFA</td>

# def all_inscription(request):
#     inscriptions = Inscription.objects.all()
#     classe = Classe.objects.all()
#     cout = classe.couts.all()
#     return render(request, 'all-inscription.html', {"inscriptions": inscriptions, "classe": classe, "cout": cout})

def all_inscription(request):
    inscriptions = Inscription.objects.select_related('etudiant', 'salleClasse__niveau').all()
    return render(request, 'all-inscription.html', {"inscriptions": inscriptions})

def add_inscription(request):
    if request.method == "POST":
        etudiant_id = request.POST["etudiant"]
        salleClasse_id = request.POST["salleClasse"]
        # coutA = request.POST["coutA"]
        montantVerse = request.POST["montantVerse"]
        
        etudiant = Etudiant.objects.get(pk=int(etudiant_id))
        salleDeClasse = SalleDeClasse.objects.get(pk=int(salleClasse_id))
        
        Inscription.objects.create(
            etudiant = etudiant,
            salleClasse = salleDeClasse,
            # coutA = coutA,
            montantVerse = montantVerse
        )
        return redirect("all_inscription")
      
    context = {
        'etudiants': Etudiant.objects.all(),
        'salles': SalleDeClasse.objects.all(),
    }
    return render(request, 'add-inscription.html', context)
    
def delete_inscription(request, id):
    inscription = Inscription.objects.get(pk=id)
    inscription.delete()
    return redirect("all_inscription")

def modifierInscription(request, id):
    inscription = Inscription.objects.get(pk=id)
    if request.method == 'POST':
        etudiant = request.POST["etudiant"]
        salleDeClasse = request.POST["salleClasse"]
        inscription.coutA = request.POST["coutA"]
        inscription.montantVerse = request.POST["montantVerse"]
        
        inscription.etudiant_id = Etudiant.objects.get(id =etudiant)
        inscription.salleClasse_id = SalleDeClasse.objects.get(id =salleDeClasse)
        
        inscription.save()
        return redirect("all_inscription")
    context = {
        'etudiants': Etudiant.objects.all(),
        'salles': SalleDeClasse.objects.all(),
        'inscription': inscription
    }
    return render(request, 'modifier-inscription.html', context)
        



#Cours

def all_cours(request):
    cours = Cours.objects.all()
    context = {'cours_list': cours}
    return render(request, 'all-cours.html', context)

def add_cours(request):
    if request.method == 'POST':
        matiere_nom = request.POST["matiere"]
        enseignant_nom = request.POST["enseignant"]
        classe_nom = request.POST["classe"]
        date_debut = request.POST["dateDebutCours"]
        duree = request.POST["dureeCours"]
        trimestre = request.POST["trimestre"]
        etat = request.POST["etat"]

        # Récupérer les objets liés à partir des noms
        matiere = Matiere.objects.get(nom=matiere_nom)
        # enseignant = Enseignant.objects.get(nom=enseignant_nom.split()[0], prenom=enseignant_nom.split()[1])
        enseignant = Enseignant.objects.get(pk=int(enseignant_nom))
        classe = Classe.objects.get(pk=int(classe_nom))

        # Création du cours
        Cours.objects.create(
            matiere=matiere,
            enseignant=enseignant,
            classe=classe,
            dateDebutCours=date_debut,
            dureeCours=duree,
            trimestre=trimestre,
            etat=etat
        )
        return redirect('all-cours')  

    context = {
        'matieres': Matiere.objects.all(),
        'enseignants': Enseignant.objects.all(),
        'classes': Classe.objects.all(),
    }
    return render(request, 'add-cours.html', context)

def modifier_cours(request, pk):
    cours = Cours.objects.get(pk=pk)
    if request.method == 'POST':
        matiere_nom = request.POST["matiere"]
        enseignant_nom = request.POST["enseignant"]
        classe_nom = request.POST["classe"]
        cours.dateDebutCours = request.POST["dateDebutCours"]
        cours.dureeCours = request.POST["dureeCours"]
        cours.trimestre = request.POST["trimestre"]
        cours.etat = request.POST["etat"]

        # Récupérer les objets liés à partir des noms
        cours.matiere = Matiere.objects.get(nom=matiere_nom)
        # enseignant = Enseignant.objects.get(nom=enseignant_nom.split()[0], prenom=enseignant_nom.split()[1])
        cours.enseignant = Enseignant.objects.get(pk=int(enseignant_nom))
        cours.classe = Classe.objects.get(pk=int(classe_nom))
        
        cours.save()
        return redirect('all-cours')
    context = {'cours': cours, 'matieres': Matiere.objects.all(), 'enseignants': Enseignant.objects.all(), 'classes': Classe.objects.all()}
    return render(request, 'modifier-cours.html', context)

def supprimer_cours(request, pk):
    Cours.objects.get(pk=pk).delete()
    return redirect('all-cours')



#Evaluation
def all_evaluation(request):
    # niveaux = Classe.objects.all()
    # evaluations = Evaluation.objects.all()
    cours = Cours.objects.all()
    # context = {'evaluations': evaluations, 'niveaux': niveaux}
    return render(request, 'all-evaluation.html', {'cours': cours})

def supprimer_evaluation(request, pk):
    Evaluation.objects.get(pk=pk).delete()
    return redirect('all_evaluation')

def modifier_evaluation(request, id):
    evaluation = Evaluation.objects.get(id=id)
    # etudiant = Etudiant.objects.get(id=id)
    
    if request.method == 'POST':
        cours_id = request.POST["cours"]
        etudiant_id = request.POST["etudiant"]
        
        evaluation.trimestre = request.POST["trimestre"]
        evaluation.typeEvaluation = request.POST["typeEvaluation"]
        evaluation.dateEvaluation = request.POST["dateEvaluation"]
        evaluation.note = request.POST["note"]

        evaluation.cours = get_object_or_404(Cours, id=cours_id)
        evaluation.etudiant = get_object_or_404(Etudiant, id=etudiant_id)

        evaluation.save()
        
        return redirect('all_evaluation')
    
    cours_list = Cours.objects.all()

    context = {
        'cours_list': cours_list,
        # 'etudiant': etudiant,
        'evaluation': evaluation
    }
    return render(request, 'modifier-evaluation.html', context)

def evaluation_groupee(request, id):
    classe = Classe.objects.get(id=id)
    inscrits = Inscription.objects.filter(
        salleClasse__niveau=classe
    ).select_related('etudiant', 'salleClasse')

    matieres = Matiere.objects.filter(niveau=classe)
    salle = SalleDeClasse.objects.get(niveau=classe)
    courrs = Cours.objects.filter(classe=classe)
    if request.method == 'POST':
        trimestre = request.POST["trimestre"]
        cours_id = request.POST["cours"]
        typeEvaluation = request.POST["typeEvaluation"]
        dateEvaluation = request.POST["dateEvaluation"]

        cours = Cours.objects.get(pk=int(cours_id))

        for inscrit in inscrits:
            note_input_name = f"note_{inscrit.etudiant.id}"
            note_val = request.POST.get(note_input_name)

            if note_val:  
                Evaluation.objects.create(
                    cours=cours,
                    etudiant=inscrit.etudiant,
                    typeEvaluation=typeEvaluation,
                    dateEvaluation=dateEvaluation,
                    note=note_val,
                    trimestre=trimestre,
                )

        return redirect('all_evaluation')  

    context = {
        'matieres': matieres,
        'salle': salle,
        'classe': classe,
        'inscrits': inscrits,
        'courrs': courrs,
    }
    return render(request, 'liste_inscrits_par_classe.html', context)

def selectClasseEvaluation(request):
    classe = Classe.objects.all()
    return render(request, 'selectClasseEvaluation.html', {'niveaux': classe})

def selectClasse(request):
    classe = Classe.objects.all()
    return render(request, 'selectClasse.html', {'niveaux': classe})

def filtre_evaluation(request, id):
    classe = Classe.objects.get(id=id)
    
    if request.method == 'POST':
        typeEvaluation = request.POST['typeEvaluation']
        nom = request.POST.get('nom')        
        
        evaluation = Evaluation.objects.filter(cours__classe=classe).select_related('etudiant', 'cours__matiere', 'cours__enseignant', 'cours__classe')
        
        evaluations = evaluation.filter(etudiant__nom__icontains = nom, typeEvaluation__icontains = typeEvaluation)
        context = {'evaluations': evaluations, 'classe': classe}
        
        return render(request, 'filtre-evaluation.html', context)
    else:
        evaluations = Evaluation.objects.filter(cours__classe=classe).select_related('etudiant', 'cours__matiere', 'cours__enseignant', 'cours__classe')
        context = {'evaluations': evaluations, 'classe': classe}
        return render(request, 'filtre-evaluation.html', context)
        
def note_individuelle(request, id):
    classe = Classe.objects.get(id=id)
    inscrits = Inscription.objects.filter(
        salleClasse__niveau=classe
    ).select_related('etudiant', 'salleClasse')

    # matieres = Matiere.objects.filter(niveau=classe)
    # salle = SalleDeClasse.objects.get(niveau=classe)
    # courrs = Cours.objects.filter(classe=classe)
   
    context = {
        'classe': classe,
        'inscrits': inscrits,
    }
    return render(request, 'note-individuelle.html', context)

def ajout_note_individuelle(request, id):
    etudiant = Etudiant.objects.get(id=id)
    
    if request.method == 'POST':
        cours_id = request.POST["cours"]
        trimestre = request.POST["trimestre"]
        type_evaluation = request.POST["typeEvaluation"]
        date_evaluation = request.POST["dateEvaluation"]
        note = request.POST["note"]
        etudiant_id = request.POST["etudiant"]

        cours = get_object_or_404(Cours, id=cours_id)
        etudiants = get_object_or_404(Etudiant, id=etudiant_id)

        Evaluation.objects.create(
            cours=cours,
            trimestre=trimestre,
            typeEvaluation=type_evaluation,
            dateEvaluation=date_evaluation,
            note=note,
            etudiant=etudiants
        )
        return redirect('all_evaluation')
    
    cours_list = Cours.objects.all()

    context = {
        'cours_list': cours_list,
        'etudiant': etudiant
    }
    return render(request, 'ajout_note_individuelle.html', context)
    

    
    
    
#coût
def all_cout(request):
    couts = Cout.objects.all()
    context = {'couts': couts}
    return render(request, 'all-cout.html', context)

def add_cout(request):
    if request.method == 'POST':
        classe_id = request.POST["classe"]
        coutInscription = request.POST['coutInscription']
        coutScolarite = request.POST['coutScolarite']
        fraisEtudeDossier = request.POST['fraisEtudeDossier']
        fraisAssocie = request.POST['fraisAssocie']
        
        classe = get_object_or_404(Classe, id=classe_id)
        if Cout.objects.filter(classe = classe).exists():
            messages.error(request, "Les coûts de cette classe ont déjà été ajoutés. veuillez modifier les coûts existants")
        
        else:
            Cout.objects.create(
                classe=classe,
                coutInscription=coutInscription,
                coutScolarite=coutScolarite,
                fraisEtudeDossier=fraisEtudeDossier,
                fraisAssocie=fraisAssocie
                )
            return redirect('all_cout')
    context = {'classe_list': Classe.objects.all()}
    return render(request, 'add-cout.html', context)

def delete_cout(request, id):
    cout = get_object_or_404(Cout, id=id)
    cout.delete()
    return redirect('all_cout')

def update_cout(request, id):
    cout = get_object_or_404(Cout, id=id)
    if request.method == 'POST':
        classe_id = request.POST["classe"]
        cout.coutInscription = request.POST['coutInscription']
        cout.coutScolarite = request.POST['coutScolarite']
        cout.fraisEtudeDossier = request.POST['fraisEtudeDossier']
        cout.fraisAssocie = request.POST['fraisAssocie']
        
        cout.classe = get_object_or_404(Classe, id=classe_id)
        
        cout.save()
        return redirect('all_cout')
    context = {'cout': cout, 'classe_list': Classe.objects.all()}
    return render(request, 'modifier-cout.html', context)





def all_subject(request):
    return render(request, 'all-subject.html')

def class_routine(request):
    return render(request, 'class-routine.html')

def student_attendance(request):
    return render(request, 'student-attendance.html')

def exam_schedule(request):
    return render(request, 'exam-schedule.html')

def exam_grade(request):
    return render(request, 'exam-grade.html')

def notice_board(request):
    return render(request, 'notice-board.html')

def reception_dossier(request):
    return render(request, 'reception-dossier.html')

def messaging(request):
    return render(request, 'messaging.html')

def account_settings(request):
    return render(request, 'account-settings.html')
