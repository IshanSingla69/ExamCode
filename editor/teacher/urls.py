from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.index, name='teacher_dashboard'),
    path('add_test', views.add_test, name='create_test'),
    path('test/<int:test_id>/question/<int:q_id>', views.add_question, name='add_question'),
    path('test/<int:test_id>/new_question/', views.new_question, name='new_question'),
]