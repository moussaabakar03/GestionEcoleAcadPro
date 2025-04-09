from django.urls import path
from . import views

urlpatterns = [
    path('eleveIndex', views.index, name='index'),
    path('index3/', views.index3, name='index3'),
    path('index4/', views.index4, name='index4'),
    path('index5/', views.index5, name='index5'),

    path('admit-form/', views.admit_form, name='admit-form'),

    path('button/', views.button, name='button'),

    path('class-routine/', views.class_routine, name='class-routine'),

    path('exam-grade/', views.exam_grade, name='exam-grade'),

    path('grid/', views.grid, name='grid'),

    path('messaging/', views.messaging, name='messaging'),

    path('modal/', views.modal, name='modal'),

    path('notice-board/', views.notice_board, name='notice-board'),

    path('notification-alart/', views.notification_alart, name='notification-alart'),

    path('progress-bar/', views.progress_bar, name='progress-bar')
    
]