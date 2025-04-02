from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def index5(request):
    return render(request, 'index5.html')

def all_student(request):
    return render(request, 'all-student.html')

def admit_form(request):
    return render(request, 'admit-form.html')

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
