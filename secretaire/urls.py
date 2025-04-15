from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index3/', views.index3, name='index3'),
    path('index4/', views.index4, name='index4'),
    path('index5/', views.index5, name='index5'),
    
    path('all-student/', views.all_student, name='all-student'),
    path('admit-form/', views.admit_form, name='admit-form'),
    path('student-promotion/', views.student_promotion, name='student-promotion'),
    path('student-detail/<str:matricule>', views.student_detail, name = 'students-detail'),
    path('detailEtudiant/<str:matricule>/<int:id>', views.detailEtudiant, name = 'detailEtudiant'),
    path('modifier_student/<str:matricule>', views.modifier_student, name = 'modifier_student'),
    path('supprimer_student/<str:matricule>', views.supprimer_student, name = 'supprimer_student'),
    path('studentParSalle/<int:id>', views.studentParSalle, name = 'studentParSalle'),
    # path('ajouter_etudiant/', views.ajouter_etudiant, name = 'ajouter_etudiant'),

    path('all-teacher/', views.all_teacher, name='all-teacher'),
    path('add-teacher/', views.add_teacher, name='add-teacher'),
    path('teacher-detail/', views.teacher_detail, name = 'teachers-detail'),
    path('detailEnseignant/<str:matricule>', views.detailEnseignant, name = 'detailEnseignant'),
    path('modifier_teacher/<str:matricule>/', views.modifier_teacher, name = 'modifier_teacher'),
    path('supprimer_teacher/<str:matricule>/', views.supprimer_teacher, name = 'supprimer_teacher'),

    path('all-parents/', views.all_parents, name='all-parents'),
    path('add-parents/', views.add_parents, name='add-parents'),
    # path('parents-detail/', views.parents_detail, name = 'parents-detail'),
    path('modifier_parent/<int:id>/', views.modifier_parent, name = 'modifier_parent'),
    path('supprimer_parent/<int:id>/', views.supprimer_parent, name = 'supprimer_parent'),


    path('all-class/', views.all_class, name='all-class'),
    path('add-class/', views.add_class, name='add-class'),
    path('supprimer_matiere/<int:id>', views.supprimer_matiere, name='supprimer_matiere'),
    path('modifier_matiere/<int:id>', views.modifier_matiere, name='modifier_matiere'),


    path('all-salle/', views.all_salle, name='all-salle'),
    path('add-salle/', views.add_salle, name='add-salle'),
    path('modifierSalle/<str:nom>', views.modifierSalle, name='modifierSalle'),
    path('supprimerSalle/<str:nom>', views.supprimerSalle, name='supprimerSalle'),
    
    
    
    path('all_niveau/', views.all_niveau, name='all_niveau'),
    path('add_niveau/', views.add_niveau, name='add_niveau'),
    
    
    
    path('all-subject/', views.all_subject, name='all-subject'),
    path('class-routine/', views.class_routine, name='class-routine'),
    path('student-attendance/', views.student_attendance, name='student-attendance'),

    path('exam-schedule/', views.exam_schedule, name='exam-schedule'),
    path('exam-grade/', views.exam_grade, name='exam-grade'),

    path('notice-board/', views.notice_board, name='notice-board'),
    path('reception-dossier/', views.reception_dossier, name='reception-dossier'),

    path('messaging/', views.messaging, name='messaging'),
    path('account-settings/', views.account_settings, name='account-settings'),
]
