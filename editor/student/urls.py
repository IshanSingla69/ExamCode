from django.urls import path
from . import views


app_name = 'student'
urlpatterns = [
    path('', views.index, name='student_dashboard'),
    path('attempt_test/<int:test_id>/question/<int:q_id>', views.attempt_test, name='attempt_test'),
    path('save_answer/<int:test_id>/question/<int:q_id>', views.save_answer, name='save_answer'),
    path('submit_test/<int:test_id>', views.submit_test, name='submit_test')
]