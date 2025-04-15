from django.contrib import messages

from django.shortcuts import get_object_or_404, render, redirect

from . models import Classe, Etudiant, Enseignant, Matiere, Parent, SalleDeClasse

def index(request):
    return render(request, 'index.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def index5(request):
    return render(request, 'index5.html')


#Etudiant
def all_student(request):
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
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
        salleDeClasse_id = request.POST["salleDeClasse"]
        # niveau = request.POST["niveau"]
        telephone = request.POST["telephone"]
        nationnalite = request.POST["nationnalite"]
        photo = request.FILES.get("photo")
        parent = request.POST.get("parent")

        # salleDeClasse_id = request.POST.get("salleDeClasse")
       
        salle = SalleDeClasse.objects.get(pk=int(salleDeClasse_id))
        parent_id = Parent.objects.get(pk=int(parent))

        
        # Vérifier si un étudiant avec le même matricule existe déjà
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
            salleDeClasse_id=salle,
            telephone=telephone,
            nationnalite=nationnalite,
            photo=photo
        )

        return redirect("all-student") 

    return render(request, "admit-form.html", {"salles": salles, "parentss": parentss})

def modifier_student(request, matricule):
    
    mtrcle = mtrcle = get_object_or_404(Etudiant, matricule=matricule)
    
    groupes_sanguins = ["A+", "A-", "B+", "B-", "O+", "O-"]
    niveaux = ["6e", "5e", "4e", "3e", "2e", "1e", "Tl"]
    sections = SalleDeClasse.objects.all()

    if request.method == "POST":
        mtrcle.nom = request.POST["nom"]
        mtrcle.prenom = request.POST["prenom"]
        mtrcle.matricule = request.POST["matricule"]
        mtrcle.genre = request.POST["genre"]
        mtrcle.date_naissance = request.POST["date_naissance"]
        mtrcle.groupe_sanguin = request.POST["groupe_sanguin"]
        mtrcle.mail = request.POST["mail"]
        # mtrcle.niveau = request.POST["niveau"]
        mtrcle.telephone = request.POST["telephone"]
        mtrcle.nationnalite = request.POST["nationnalite"]
        mtrcle.photo = request.FILES.get("photo")
        mtrcle.salleDeClasse = SalleDeClasse.objects.get(pk=int(request.POST["salleDeClasse"]))

        mtrcle.save()
        return redirect("all-student")
    

    return render(request, "modifier-student.html", {
        "student": mtrcle,
        "groupes_sanguins": groupes_sanguins,
        "niveaux": niveaux,
        "sections": sections,
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
    context = {"etudiant": etudiant }
    return render(request, 'student-details.html', context)

def detailEtudiant(request, matricule, id):
    etudiant = Etudiant.objects.get(matricule = matricule)
    parent = Parent.objects.get(id = id)
    context = {"etudiant": etudiant, "parent": parent }
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
    students = Etudiant.objects.filter(salleDeClasse_id=id)
    salle = SalleDeClasse.objects.get(pk=id)
    return render(request, 'studentParSalle.html', {"etudiant": students, "salle": salle})



#Classe(niveau)
def all_niveau(request):
    niveaux = Classe.objects.all()
    return render(request, 'all-niveau.html', {"niveaux": niveaux})

def add_niveau(request):
    if request.method == "POST":
        classe = request.POST["classe"]
        capacite = int(request.POST["capacite"])
        scolarite = request.POST["scolarite"]
        
        Classe.objects.create(
            classe = classe,
            capacite = capacite,
            scolarite = scolarite
        )
        return redirect("all_niveau")
    return render(request, 'add-niveau.html')



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
