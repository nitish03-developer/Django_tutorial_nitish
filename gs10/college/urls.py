from django.urls import path
from . import views
urlpatterns = [
    path('Name/', views.college_name)
]
