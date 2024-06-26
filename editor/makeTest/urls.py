from django.urls import path
from . import views
app_name = "makeTest"

urlpatterns = [
    path('', views.create_test, name='create_test'),
    path('test/<int:test_id>/question/<int:q_id>', views.add_question, name='add_question'),
    path('makeTest/test/<int:test_id>/question/', views.view_question, name='view_question'),
    path('test/<int:test_id>/new_question/', views.new_question, name='new_question'),
    path('test/<int:test_id>/delete_test/', views.delete_test, name='delete_test'),
    path('test/<int:test_id>/delete_question/<int:q_id>', views.delete_question, name='delete_question'),
    path('test/<int:test_id>/publish/', views.publish, name='publish'),

]