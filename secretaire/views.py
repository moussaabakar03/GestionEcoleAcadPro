from django.shortcuts import get_object_or_404, render, redirect

from . models import Etudiant, Enseignant, Matiere, Parent, SalleDeClasse

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
        mtrcle.salleDeClasse = request.POST["salleDeClasse"]
        # mtrcle.niveau = request.POST["niveau"]
        mtrcle.telephone = request.POST["telephone"]
        mtrcle.nationnalite = request.POST["nationnalite"]
        mtrcle.photo = request.FILES.get("photo")
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

def student_detail(request):
    return render(request, 'student-details.html')

def detailEtudiant(request, matricule):
    etudiant = Etudiant.objects.get(matricule = matricule)
    context = {"etudiant": etudiant }
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
        groupe_sanguin = request.POST["groupe_sanguin"]
        diplome = request.POST["diplome"]
        profession = request.POST["profession"]
        email = request.POST["email"]
        section = request.POST["section"]
        phone = request.POST["phone"]
        photo = request.FILES.get("photo")  
    
        Enseignant.objects.create( matricule = matricule, nom = nom, prenom = prenom, profession = profession, tel = phone, 
                                diplome = diplome,  photo = photo , date_naissance = date_naissance, sexe = sexe, mail = email)
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
        enseignant.mail = request.POST["email"]
        enseignant.save()
        return redirect("all-teacher")
    return render(request, 'modifier-teacher.html', {"enseignant": enseignant, "groupes_sanguins": groupes_sanguins})

def supprimer_teacher(request, matricule):
    enseignant = Enseignant.objects.get(matricule = matricule)
    enseignant.delete()
    return redirect("all-teacher")



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

def parents_detail(request):
    return render(request, 'parents-details.html')



#Matiere
def all_class(request):
    matiere = Matiere.objects.all()
    return render(request, 'all-class.html', {"matieres": matiere})

def add_class(request):
    enseignants = Enseignant.objects.all()
    content = {"enseignants": enseignants }
    if request.method == "POST":
        nom = request.POST["nom"]
        niveau = request.POST["niveau"]
        coefficient = request.POST["coefficient"]
        description = request.POST.get("description", "")  # facultatif
        enseignant_id = request.POST["enseignant"]
        enseignant = Enseignant.objects.get(pk=int(enseignant_id))
        Matiere.objects.create(
            nom=nom,
            niveau=niveau,
            coefficient=coefficient,
            description=description,
            enseignant=enseignant
        )

        return redirect("all-class")
    return render(request, 'add-class.html', content)



#salle de classe
def all_salle(request):
    salles = SalleDeClasse.objects.all()
    return render(request, 'all-salle.html', {"salles": salles})

def add_salle(request):
    if request.method == "POST":
        nom = request.POST["nom"]
        capacite = int(request.POST["capacite"])
        niveau = request.POST["niveau"]
        emplacement = request.POST.get("emplacement", "")  # facultatif

        SalleDeClasse.objects.create(
            nom=nom,
            capacite=capacite,
            emplacement=emplacement,
            niveau = niveau
        )

        return redirect("all-salle") 

    return render(request, 'add-salle.html')

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
