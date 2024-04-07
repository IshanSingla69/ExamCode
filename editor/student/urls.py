from django.urls import path
from . import views


app_name = 'student'
urlpatterns = [
    path('', views.index, name='student_dashboard'),
    path('attempt_test/<int:test_id>/question/<int:q_id>', views.attempt_test, name='attempt_test'),
]