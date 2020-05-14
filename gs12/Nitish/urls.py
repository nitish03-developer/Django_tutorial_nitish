from django.urls import path
from . import views
urlpatterns = [
    path('nitishdj/', views.nitish_dj),
    path('nitishpy/', views.nitish_py),
]