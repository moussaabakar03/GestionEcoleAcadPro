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
    path('student-detail/', views.student_detail, name = 'students-detail'),

    path('all-teacher/', views.all_teacher, name='all-teacher'),
    path('add-teacher/', views.add_teacher, name='add-teacher'),
    path('teacher-detail/', views.teacher_detail, name = 'teachers-detail'),

    path('all-parents/', views.all_parents, name='all-parents'),
    path('add-parents/', views.add_parents, name='add-parents'),
    path('parents-detail/', views.parents_detail, name = 'parents-detail'),

    path('all-class/', views.all_class, name='all-class'),
    path('add-class/', views.add_class, name='add-class'),

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
