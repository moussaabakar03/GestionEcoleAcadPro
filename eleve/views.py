from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'partial\index.html')

def index3(request):
    return render(request, 'index3.html')

def index4(request):
    return render(request, 'index4.html')

def index5(request):
    return render(request, 'index5.html')

def admit_form(request):
    return render(request, 'admit-form.html')

def button(request):
    return render(request, 'button.html')

def class_routine(request):
    return render(request, 'class-routine.html')

def exam_grade(request):
    return render(request, 'exam-grade.html')

def grid(request):
    return render(request, 'grid.html')

def messaging(request):
    return render(request, 'partial/messaging.html')

def modal(request):
    return render(request, 'modal.html')

def notice_board(request):
    return render(request, 'notice-board.html')

def notification_alart(request):
    return render(request, 'notification-alart.html')

def progress_bar(request):
    return render(request, 'progress-bar.html')