from django.urls import path
from . import views
urlpatterns = [
    path('mahato/', views.mahato_dj),
]