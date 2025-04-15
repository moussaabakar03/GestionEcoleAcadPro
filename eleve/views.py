from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'partial\index.html')

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
    return render(request, 'partial/payements.html')