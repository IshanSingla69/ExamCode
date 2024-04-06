from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.index, name='teacher_dashboard'),
    path('add_test/', views.add_test, name='add_test'),
    path('add_question/', views.add_question, name='add_question'),
]