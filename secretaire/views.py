from django.shortcuts import render, redirect

from . models import Etudiant

def index(request):
    return render(request, 'index.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def index5(request):
    return render(request, 'index5.html')

def all_student(request):
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
    return render(request, 'all-student.html', context)

def admit_form(request):
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        matricule = request.POST["matricule"]
        genre = request.POST["genre"]
        date_naissance = request.POST["date_naissance"]
        groupe_sanguin = request.POST["groupe_sanguin"]
        mail = request.POST["mail"]
        salleDeClasse = request.POST["salleDeClasse"]
        niveau = request.POST["niveau"]
        telephone = request.POST["telephone"]
        nationnalite = request.POST["nationnalite"]
        photo = request.FILES.get("photo")

        # Vérifier si un étudiant avec le même matricule existe déjà
        if Etudiant.objects.filter(matricule=matricule).exists():
            return render(request, "admit-form.html", {"error": "Matricule déjà utilisé !"})

        # Enregistrement dans la base de données
        Etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            matricule=matricule,
            genre=genre,
            date_naissance=date_naissance,
            groupe_sanguin=groupe_sanguin,
            mail=mail,
            salleDeClasse=salleDeClasse,
            niveau=niveau,
            telephone=telephone,
            nationnalite=nationnalite,
            photo=photo
        )

        return redirect("all-student")  # Redirection après ajout

    return render(request, "admit-form.html")

# def admit_form(request):
#     return render(request, 'admit-form.html')

def student_promotion(request):
    return render(request, 'student-promotion.html')

def student_detail(request):
    return render(request, 'student-details.html')

def all_teacher(request):
    return render(request, 'all-teacher.html')

def add_teacher(request):
    return render(request, 'add-teacher.html')

def teacher_detail(request):
    return render(request, 'teacher-details.html')

def all_parents(request):
    return render(request, 'all-parents.html')

def add_parents(request):
    return render(request, 'add-parents.html')

def parents_detail(request):
    return render(request, 'parents-details.html')

def all_class(request):
    return render(request, 'all-class.html')

def add_class(request):
    return render(request, 'add-class.html')

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
