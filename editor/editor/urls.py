from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('student/', include('student.urls')),
<<<<<<< HEAD
    
=======
    path('teacher/', include('teacher.urls')),
>>>>>>> 2a8ee6e985f0a54c575c240b9f2c97ad16f10442
]
