from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index3(request):
    return render(request, 'partial/partial/index3.html')

def index4(request):
    return render(request, 'partial/index4.html')

def index5(request):
    return render(request, 'partial/index5.html')

def admit_form(request):
    return render(request, 'partial/admit-form.html')

def button(request):
    return render(request, 'partial/button.html')

def class_routine(request):
    return render(request, 'partial/class-routine.html')

def exam_grade(request):
    return render(request, 'partial/exam-grade.html')

def grid(request):
    return render(request, 'partial/grid.html')

def messaging(request):
    return render(request, 'partial/messaging.html')

def modal(request):
    return render(request, 'partial/modal.html')

def notice_board(request):
    return render(request, 'partial/notice-board.html')

def notification_alart(request):
    return render(request, 'partial/notification-alart.html')

def progress_bar(request):
    return render(request, 'partial/progress-bar.html')

def presence(request):
    return render(request, 'partial/presence.html')

def payements(request):
    return render(request, 'partial/payments.html')






def compteEtudiant(request, matricule, id):
    etudiant = Etudiant.objects.get(matricule=matricule)
    inscriptions = etudiant.inscriptions.all()

    somme_notes_ponderees = 0.0
    somme_coefficients = 0
    
    if request.method == "POST":
        # moyenne = 0.0
        
        matiere = request.POST['matiere']
        trimestre = request.POST['trimestre']
        typeEvaluation = request.POST['typeEvaluation']
        
        evaluations = etudiant.evaluations.all()
        
        if matiere:
            evaluations = etudiant.evaluations.filter(cours__matiere__nom__contains = matiere.strip())
            for evaluation in evaluations:
                coefficient = evaluation.cours.matiere.coefficient
                somme_notes_ponderees += float(evaluation.note) * coefficient
                somme_coefficients += coefficient
        elif trimestre:
            evaluations = etudiant.evaluations.filter(trimestre__contains = trimestre.strip())
            for evaluation in evaluations:
                coefficient = evaluation.cours.matiere.coefficient
                somme_notes_ponderees += float(evaluation.note) * coefficient
                somme_coefficients += coefficient
        elif typeEvaluation:
            evaluations = etudiant.evaluations.filter(typeEvaluation__contains = typeEvaluation.strip())
            for evaluation in evaluations:
                coefficient = evaluation.cours.matiere.coefficient
                somme_notes_ponderees += float(evaluation.note) * coefficient
                somme_coefficients += coefficient
        elif matiere and trimestre and typeEvaluation:
            evaluations = etudiant.evaluations.filter(typeEvaluation__contains = typeEvaluation, trimestre__contains = trimestre, cours__matiere__nom__contains = matiere.strip())
            for evaluation in evaluations:
                coefficient = evaluation.cours.matiere.coefficient
                somme_notes_ponderees += float(evaluation.note) * coefficient
                somme_coefficients += coefficient
        
        moyenne = round(somme_notes_ponderees / somme_coefficients, 2) if somme_coefficients != 0 else 0.0
        
        context = {
            "etudiant": etudiant,
            "evaluations": evaluations,
            "moyenne": moyenne
            }
        return render(request, 'compteEtudiant.html', context)
        
        
    else:    
        evaluations = etudiant.evaluations.all()
        for evaluation in evaluations:
            coefficient = evaluation.cours.matiere.coefficient
            somme_notes_ponderees += float(evaluation.note) * coefficient
            somme_coefficients += coefficient

        moyenne = round(somme_notes_ponderees / somme_coefficients, 2) if somme_coefficients != 0 else 0.0

        context = {
            "etudiant": etudiant,
            "evaluations": evaluations,
            "moyenne": moyenne
        }
        return render(request, 'compteEtudiant.html', context)
