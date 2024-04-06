from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('makeTest/', include('makeTest.urls')),
]
