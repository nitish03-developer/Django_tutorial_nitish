from django.urls import path
from . import views
urlpatterns = [
    path('Name/', views.student_name)
]
